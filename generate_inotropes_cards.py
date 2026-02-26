#!/usr/bin/env python3
"""
Generate CCRN Inotropes & Vasopressors Anki deck
Source: extracted/inotropes_handbook.txt ONLY
"""

import genanki
import random
import csv
import os

# ── Stable IDs (deterministic) ──────────────────────────────────────────────
MODEL_ID  = 1234567890
DECK_ID   = 9876543210
DECK_NAME = "CCRN - Inotropes & Vasopressors (ICU Masterclass)"

model = genanki.Model(
    MODEL_ID,
    "CCRN Basic",
    fields=[
        {"name": "Question"},
        {"name": "Answer"},
        {"name": "Tags"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "<div class='question'>{{Question}}</div>",
            "afmt": (
                "{{FrontSide}}"
                "<hr id='answer'>"
                "<div class='answer'>{{Answer}}</div>"
            ),
        }
    ],
    css=(
        ".card { font-family: Arial, sans-serif; font-size: 16px; "
        "text-align: left; padding: 10px; } "
        ".question { font-weight: bold; margin-bottom: 8px; } "
        ".answer { color: #333; } "
    ),
)

# ── Card definitions ─────────────────────────────────────────────────────────
# Format: (question, answer, [extra_tags])
# Base tag ccrn::pharmacology is always added.

RAW_CARDS = [

    # ═══════════════════════════════════════════════════════════════════════
    # DEFINITIONS / PHYSIOLOGY
    # ═══════════════════════════════════════════════════════════════════════
    ("What is a vasopressor?",
     "Agent that causes vascular constriction (venous or arterial); raises blood pressure.",
     ["definitions"]),

    ("What is an inotrope?",
     "Agent that affects the force of myocardial contraction.",
     ["definitions"]),

    ("What is a positive inotrope?",
     "Agent that increases myocardial contractility (e.g., epinephrine, dobutamine).",
     ["definitions"]),

    ("What is a negative inotrope?",
     "Agent that decreases myocardial contractility (e.g., beta-blockers).",
     ["definitions"]),

    ("What is an inodilator?",
     "Agent with combined inotropic + vasodilatory effects (e.g., dobutamine, milrinone).",
     ["definitions"]),

    ("What is an inopressor?",
     "Agent with combined inotropic + vasopressor effects (e.g., epinephrine at high dose).",
     ["definitions"]),

    ("What is a chronotropic agent?",
     "Agent that increases heart rate by affecting the electrical system (e.g., epinephrine).",
     ["definitions"]),

    ("What is a dromotropic agent?",
     "Agent that increases conduction speed through the AV node (e.g., epinephrine).",
     ["definitions"]),

    ("What is a lusitropic agent?",
     "Agent that promotes diastolic relaxation; catecholamines are positive lusitropes.",
     ["definitions"]),

    ("What is bathmotropy?",
     "Myocardial excitability; positive bathmotropy brings resting membrane potential closer to depolarization threshold.",
     ["definitions"]),

    # ═══════════════════════════════════════════════════════════════════════
    # SHOCK
    # ═══════════════════════════════════════════════════════════════════════
    ("What are the 4 main classes of shock?",
     "Hypovolemic; Distributive; Cardiogenic; Obstructive",
     ["shock"]),

    ("How is shock defined?",
     "Inadequate organ perfusion.",
     ["shock"]),

    ("What is the first-line treatment for hypovolemic shock?",
     "Volume resuscitation.",
     ["shock"]),

    ("What is the first-line treatment for distributive shock?",
     "Vasopressors to increase SVR.",
     ["shock"]),

    ("What is the first-line treatment for cardiogenic shock?",
     "Inotropy or mechanical circulatory support.",
     ["shock"]),

    ("What distinguishes distributive from hypovolemic shock on echo?",
     "Both have low afterload; hypovolemic also has low preload; distributive has adequate preload.",
     ["shock"]),

    # ═══════════════════════════════════════════════════════════════════════
    # RECEPTORS
    # ═══════════════════════════════════════════════════════════════════════
    ("What are the hemodynamic effects of alpha-1 receptor activation?",
     "Smooth muscle contraction; vasoconstriction; increased arterial pressure; sphincter contraction.",
     ["receptors"]),

    ("What are the hemodynamic effects of alpha-2 receptor activation?",
     "May lower blood pressure and heart rate; alters norepinephrine neurotransmitter function.",
     ["receptors"]),

    ("What are the hemodynamic effects of beta-1 receptor activation?",
     "Increased heart rate (chronotropy); increased contractility (inotropy); increased cardiac output (dromotropy).",
     ["receptors"]),

    ("What are the hemodynamic effects of beta-2 receptor activation?",
     "Smooth muscle relaxation; lowers intravascular pressure (vasodilation).",
     ["receptors"]),

    ("What are the effects of beta-3 receptor activation?",
     "Increased lipolysis; bladder relaxation; no major hemodynamic effects.",
     ["receptors"]),

    ("What are the hemodynamic effects of dopamine receptor activation?",
     "Vasodilation; promotes diuresis (renal artery vasodilation).",
     ["receptors", "dopamine"]),

    ("What are the effects of V1 vasopressin receptor activation?",
     "Vasoconstriction; no effect on pulmonary vasculature; may promote thrombosis.",
     ["receptors", "vasopressin"]),

    ("Where are V1 vasopressin receptors located?",
     "Vascular smooth muscle and platelets.",
     ["receptors", "vasopressin"]),

    ("What are the effects of V2 vasopressin receptor activation?",
     "Antidiuretic effect (water resorption in renal collecting ducts).",
     ["receptors", "vasopressin"]),

    ("What are the effects of V3 vasopressin receptor activation?",
     "Promotes corticotropin release from anterior pituitary → steroid-mediated hemodynamic response.",
     ["receptors", "vasopressin"]),

    ("What are the effects of Angiotensin II (type 1) receptor activation?",
     "Vasoconstriction; aldosterone production; vasopressin release; decreased renal blood flow.",
     ["receptors", "angiotensin"]),

    # ═══════════════════════════════════════════════════════════════════════
    # MYOCYTE CONTRACTION
    # ═══════════════════════════════════════════════════════════════════════
    ("What is the role of the L-type calcium channel in myocyte contraction?",
     "Membrane depolarization opens it → calcium influx → triggers calcium release from sarcoplasmic reticulum via ryanodine receptors → contraction.",
     ["physiology"]),

    ("How does beta-1 receptor activation increase contractility?",
     "Beta-1 → increases cAMP → potentiates L-type Ca²⁺ channel → increased calcium influx → increased contractility.",
     ["physiology", "receptors"]),

    ("How does milrinone increase contractility at the cellular level?",
     "Inhibits PDE-III → prevents cAMP breakdown → increased cAMP → calcium-induced calcium release → contraction.",
     ["physiology", "milrinone"]),

    # ═══════════════════════════════════════════════════════════════════════
    # MONITORING
    # ═══════════════════════════════════════════════════════════════════════
    ("What does serum lactate indicate in shock?",
     "Global estimate of tissue hypoperfusion; confounded by epinephrine-induced release and sepsis.",
     ["monitoring"]),

    ("What is central venous oxygen saturation (ScvO2) used for in shock?",
     "Estimates cardiac output using Fick's law; low ScvO2 suggests inadequate oxygen delivery.",
     ["monitoring"]),

    ("What is the square wave test used for?",
     "Identifies over- or under-dampening of an arterial line pressure conduit.",
     ["monitoring"]),

    ("What does pulse pressure reflect?",
     "Relative strength of cardiac contraction; wider PP = stronger contraction.",
     ["monitoring"]),

    # ═══════════════════════════════════════════════════════════════════════
    # PHENYLEPHRINE
    # ═══════════════════════════════════════════════════════════════════════
    ("What is phenylephrine?",
     "Vasopressor; pure alpha-1 agonist; raises SVR with no beta activity.",
     ["phenylephrine"]),

    ("What receptors does phenylephrine activate?",
     "Alpha-1 only (no beta activity).",
     ["phenylephrine", "receptors"]),

    ("What is phenylephrine's effect on heart rate?",
     "Reflexive decrease (reflex bradycardia) due to rising BP without beta agonism.",
     ["phenylephrine"]),

    ("What is phenylephrine's effect on cardiac output?",
     "May decrease CO by increasing afterload.",
     ["phenylephrine"]),

    ("What is phenylephrine's effect on SVR?",
     "Increases SVR (pure vasoconstriction).",
     ["phenylephrine"]),

    ("What is phenylephrine's effect on preload?",
     "Increases venous return (mild increase in preload via venoconstriction).",
     ["phenylephrine"]),

    ("What is phenylephrine's effect on afterload?",
     "Increases afterload significantly.",
     ["phenylephrine"]),

    ("When is phenylephrine preferred clinically?",
     "SVT with hypotension; pure distributive shock when tachycardia must be avoided; vasoplegic states without cardiac dysfunction.",
     ["phenylephrine"]),

    ("When should phenylephrine be avoided?",
     "RV dysfunction (increases RV afterload, no inotropy); cardiogenic shock.",
     ["phenylephrine"]),

    ("What is phenylephrine's major adverse effect?",
     "Reflex bradycardia; pulmonary vasoconstriction; decreased CO.",
     ["phenylephrine"]),

    ("What is the typical dose range for phenylephrine infusion?",
     "10–200 mcg/min.",
     ["phenylephrine"]),

    ("What is a push-dose of phenylephrine?",
     "100 mcg/mL concentration; 1–2 mL bolus for immediate BP support.",
     ["phenylephrine"]),

    # ═══════════════════════════════════════════════════════════════════════
    # NOREPINEPHRINE
    # ═══════════════════════════════════════════════════════════════════════
    ("What is norepinephrine?",
     "Vasopressor/Inopressor; potent alpha-adrenergic agonist with mild beta-adrenergic agonism; first-line for most shock.",
     ["norepi", "norepinephrine"]),

    ("What receptors does norepinephrine activate?",
     "Primarily alpha-1 (strong); mild beta-1 agonism.",
     ["norepi", "norepinephrine", "receptors"]),

    ("What is norepinephrine's effect on SVR?",
     "Increases SVR (potent vasoconstriction).",
     ["norepi", "norepinephrine"]),

    ("What is norepinephrine's effect on heart rate?",
     "Mild increase or unchanged (mild beta-1); often offset by baroreflex.",
     ["norepi", "norepinephrine"]),

    ("What is norepinephrine's effect on cardiac output?",
     "Mildly increases CO via beta-1 inotropy; may decrease if afterload dominates.",
     ["norepi", "norepinephrine"]),

    ("What is norepinephrine's effect on preload?",
     "Increases preload (venoconstriction).",
     ["norepi", "norepinephrine"]),

    ("What is norepinephrine's effect on afterload?",
     "Increases afterload significantly.",
     ["norepi", "norepinephrine"]),

    ("When is norepinephrine preferred clinically?",
     "First-line agent for undifferentiated shock and septic shock.",
     ["norepi", "norepinephrine"]),

    ("What is norepinephrine's major adverse effect?",
     "Tissue necrosis if extravasation occurs; ischemia at high doses.",
     ["norepi", "norepinephrine"]),

    ("Why is central venous access preferred for norepinephrine?",
     "Potent vasoconstrictor; extravasation risk causes tissue necrosis.",
     ["norepi", "norepinephrine"]),

    ("What is the typical dose range for norepinephrine?",
     "0.01–3 mcg/kg/min (or 1–30 mcg/min).",
     ["norepi", "norepinephrine"]),

    ("What are norepinephrine titration pearls?",
     "Titrate to MAP goal (≥65 mmHg); add vasopressin to spare norepinephrine dose; central line preferred.",
     ["norepi", "norepinephrine"]),

    # ═══════════════════════════════════════════════════════════════════════
    # EPINEPHRINE
    # ═══════════════════════════════════════════════════════════════════════
    ("What is epinephrine?",
     "Inopressor/Catecholamine; agonist at all adrenergic receptors (alpha-1, beta-1, beta-2); dose-dependent effects.",
     ["epi", "epinephrine"]),

    ("What receptors does epinephrine activate?",
     "All adrenergic: alpha-1, alpha-2, beta-1, beta-2.",
     ["epi", "epinephrine", "receptors"]),

    ("What is epinephrine's effect at low doses?",
     "Beta effects dominate: increased HR, contractility, smooth muscle relaxation (beta-2 vasodilation).",
     ["epi", "epinephrine"]),

    ("What is epinephrine's effect at high doses?",
     "Alpha-1 dominates: vasoconstriction, increased SVR.",
     ["epi", "epinephrine"]),

    ("What is epinephrine's effect on SVR?",
     "Dose-dependent: low dose may decrease SVR (beta-2); high dose increases SVR (alpha-1).",
     ["epi", "epinephrine"]),

    ("What is epinephrine's effect on heart rate?",
     "Increases HR (beta-1 chronotropy).",
     ["epi", "epinephrine"]),

    ("What is epinephrine's effect on cardiac output?",
     "Increases CO (positive inotropy + chronotropy).",
     ["epi", "epinephrine"]),

    ("What is epinephrine's effect on preload?",
     "Increases preload (venoconstriction at alpha doses).",
     ["epi", "epinephrine"]),

    ("What is epinephrine's effect on afterload?",
     "Dose-dependent: increases afterload at higher doses.",
     ["epi", "epinephrine"]),

    ("When is epinephrine preferred clinically?",
     "Cardiogenic shock with hypotension; anaphylaxis; cardiac arrest; second-line septic shock; beta-blocker/CCB overdose.",
     ["epi", "epinephrine"]),

    ("What is epinephrine's major adverse effect?",
     "Tachyarrhythmias; elevated lactate (may confound perfusion assessment); myocardial ischemia.",
     ["epi", "epinephrine"]),

    ("Why does epinephrine elevate lactate?",
     "Causes increased lactate production and release independent of tissue hypoperfusion.",
     ["epi", "epinephrine"]),

    ("What is the typical infusion dose range for epinephrine?",
     "0.01–0.3 mcg/kg/min.",
     ["epi", "epinephrine"]),

    ("What is the cardiac arrest dose of epinephrine?",
     "1 mg IV bolus (traditional).",
     ["epi", "epinephrine"]),

    ("What is a push-dose of epinephrine?",
     "10 mcg/mL concentration; 1–2 mL bolus IV for immediate BP/HR support.",
     ["epi", "epinephrine"]),

    ("What is an advantage of epinephrine over norepinephrine for extravasation?",
     "Epinephrine is tolerated subcutaneously; norepinephrine causes tissue necrosis.",
     ["epi", "epinephrine", "norepi"]),

    # ═══════════════════════════════════════════════════════════════════════
    # DOBUTAMINE
    # ═══════════════════════════════════════════════════════════════════════
    ("What is dobutamine?",
     "Inodilator/Inotrope; synthetic beta-agonist; preferentially activates beta-1 (3× beta-1 vs beta-2); mild alpha activity.",
     ["dobutamine"]),

    ("What receptors does dobutamine activate?",
     "Beta-1 (preferential, 3:1 over beta-2); mild beta-2; mild alpha-1.",
     ["dobutamine", "receptors"]),

    ("What is dobutamine's effect on SVR?",
     "Decreases SVR (vasodilation via beta-2).",
     ["dobutamine"]),

    ("What is dobutamine's effect on heart rate?",
     "Increases HR (beta-1 chronotropy).",
     ["dobutamine"]),

    ("What is dobutamine's effect on cardiac output?",
     "Increases CO (positive inotropy + decreased afterload).",
     ["dobutamine"]),

    ("What is dobutamine's effect on preload?",
     "Mildly decreases preload (vasodilation).",
     ["dobutamine"]),

    ("What is dobutamine's effect on afterload?",
     "Decreases afterload (inodilator).",
     ["dobutamine"]),

    ("When is dobutamine preferred clinically?",
     "First-line inotrope for cardiogenic shock; RV failure; high SVR states; valvular regurgitation.",
     ["dobutamine"]),

    ("What is dobutamine's major adverse effect?",
     "Hypotension; tachyarrhythmias; increased myocardial oxygen demand.",
     ["dobutamine"]),

    ("What is the typical dose range for dobutamine?",
     "2–15 mcg/kg/min (occasionally higher).",
     ["dobutamine"]),

    ("What are dobutamine weaning considerations?",
     "Taper gradually; monitor for rebound hemodynamic deterioration; assess underlying cause of shock.",
     ["dobutamine"]),

    # ═══════════════════════════════════════════════════════════════════════
    # ISOPROTERENOL
    # ═══════════════════════════════════════════════════════════════════════
    ("What is isoproterenol?",
     "Inotrope/Chronotrope; synthetic nonselective beta-agonist; no alpha activity; strong chronotropic effect.",
     ["isoproterenol"]),

    ("What receptors does isoproterenol activate?",
     "Beta-1 and beta-2 (nonselective); no alpha activity.",
     ["isoproterenol", "receptors"]),

    ("What is isoproterenol's effect on SVR?",
     "Decreases SVR (beta-2 vasodilation); causes hypotension.",
     ["isoproterenol"]),

    ("What is isoproterenol's effect on heart rate?",
     "Profound increase in HR (strongest chronotrope among inotropes).",
     ["isoproterenol"]),

    ("What is isoproterenol's effect on cardiac output?",
     "Increases CO (strong inotropy + chronotropy).",
     ["isoproterenol"]),

    ("When is isoproterenol preferred clinically?",
     "Symptomatic bradycardia (best chronotropic agent); bridge to pacing; Torsades de Pointes; heart transplant bradycardia.",
     ["isoproterenol"]),

    ("What is isoproterenol's major adverse effect?",
     "Significant hypotension (vasodilation); tachyarrhythmias; high cost.",
     ["isoproterenol"]),

    ("What is the typical dose range for isoproterenol?",
     "0.5–5 mcg/min (up to 20 mcg/min for severe bradycardia).",
     ["isoproterenol"]),

    # ═══════════════════════════════════════════════════════════════════════
    # DOPAMINE
    # ═══════════════════════════════════════════════════════════════════════
    ("What is dopamine?",
     "Indirect-acting vasopressor/Inotrope; precursor to norepinephrine/epinephrine; dose-dependent receptor effects.",
     ["dopamine"]),

    ("How does dopamine exert most of its hemodynamic effects?",
     "Converts to norepinephrine and epinephrine (indirect mechanism); direct dopamine receptor effects at low doses.",
     ["dopamine"]),

    ("What are dopamine's effects at low doses (1–5 mcg/kg/min)?",
     "Dopamine receptor activation → renal/mesenteric vasodilation, increased diuresis, natriuresis.",
     ["dopamine"]),

    ("What are dopamine's effects at medium doses (5–15 mcg/kg/min)?",
     "Beta-receptor effects → increased HR, contractility, cardiac output.",
     ["dopamine"]),

    ("What are dopamine's effects at high doses (>15 mcg/kg/min)?",
     "Alpha-1 activation → vasoconstriction, increased BP, increased SVR.",
     ["dopamine"]),

    ("What receptors does dopamine activate?",
     "Dopamine receptors (low dose); beta-1/2 (mid dose); alpha-1 (high dose).",
     ["dopamine", "receptors"]),

    ("What is dopamine's effect on SVR?",
     "Dose-dependent: decreases at low dose (vasodilation); increases at high dose (vasoconstriction).",
     ["dopamine"]),

    ("What is dopamine's effect on heart rate?",
     "Increases HR (especially at medium/high doses).",
     ["dopamine"]),

    ("What is dopamine's effect on cardiac output?",
     "Increases CO at medium doses; variable at high doses.",
     ["dopamine"]),

    ("When is dopamine preferred clinically?",
     "Rarely first-line; may be used for bradycardia-associated hypotension; alternative if norepi unavailable.",
     ["dopamine"]),

    ("Does low-dose dopamine protect the kidneys?",
     "No; despite promoting diuresis, low-dose dopamine has not shown clinically important renoprotective effects.",
     ["dopamine"]),

    ("What is dopamine's major adverse effect?",
     "Unpredictable dose-response; tachyarrhythmias; tissue necrosis with extravasation.",
     ["dopamine"]),

    ("Why is dopamine no longer first-line for shock?",
     "Unpredictable pharmacodynamics; higher rate of arrhythmias compared to norepinephrine; safer alternatives exist.",
     ["dopamine"]),

    # ═══════════════════════════════════════════════════════════════════════
    # EPHEDRINE
    # ═══════════════════════════════════════════════════════════════════════
    ("What is ephedrine?",
     "Indirect-acting sympathomimetic; stimulates norepinephrine release; effects similar to low-dose epinephrine.",
     ["ephedrine"]),

    ("What is ephedrine's mechanism of action?",
     "Stimulates norepinephrine release from sympathetic terminals (indirect catecholamine release).",
     ["ephedrine"]),

    ("When may ephedrine be less effective?",
     "Catecholamine depletion states (prolonged critical illness).",
     ["ephedrine"]),

    ("What is the typical dose of ephedrine?",
     "5–10 mg IV bolus; 25–50 mg IM.",
     ["ephedrine"]),

    # ═══════════════════════════════════════════════════════════════════════
    # VASOPRESSIN
    # ═══════════════════════════════════════════════════════════════════════
    ("What is vasopressin?",
     "Vasopressor/ADH; naturally occurring nonapeptide from posterior pituitary; V1-mediated vasoconstriction; V2-mediated antidiuresis.",
     ["vasopressin"]),

    ("What receptors does vasopressin activate?",
     "V1 (vasoconstriction on smooth muscle/platelets); V2 (antidiuresis); V3 (corticotropin release).",
     ["vasopressin", "receptors"]),

    ("What is vasopressin's effect on SVR?",
     "Increases SVR (vasoconstriction via V1 receptors).",
     ["vasopressin"]),

    ("What is vasopressin's effect on pulmonary vascular resistance?",
     "Does NOT increase pulmonary vascular resistance (advantage over catecholamines).",
     ["vasopressin"]),

    ("What is vasopressin's effect on heart rate?",
     "No direct chronotropic effect; HR may decrease reflexively with rising BP.",
     ["vasopressin"]),

    ("What is vasopressin's effect on preload?",
     "Mild increase (venoconstriction); V2 also increases water reabsorption.",
     ["vasopressin"]),

    ("What is vasopressin's effect on afterload?",
     "Increases afterload (systemic vasoconstriction).",
     ["vasopressin"]),

    ("What is vasopressin's effect on cardiac output?",
     "May decrease CO if afterload increases without inotropy.",
     ["vasopressin"]),

    ("What is a key advantage of vasopressin over catecholamines in acidosis?",
     "Effect is NOT pH-sensitive; catecholamine receptors have diminished response in acidic environments.",
     ["vasopressin"]),

    ("When is vasopressin preferred clinically?",
     "Adjunct to norepinephrine in septic shock; RV failure (no pulmonary vasoconstriction); refractory shock; esophageal variceal bleeding.",
     ["vasopressin"]),

    ("What is vasopressin's major adverse effect?",
     "Splanchnic ischemia (especially at high doses); hyponatremia; thrombosis (platelet activation via V1).",
     ["vasopressin"]),

    ("What is the standard vasopressin infusion dose?",
     "0.01–0.04 units/min (physiologic supplementation).",
     ["vasopressin"]),

    ("What is the high-dose vasopressin range and its indication?",
     "Up to 0.1 units/min for esophageal variceal bleeding; risk of splanchnic ischemia at this dose.",
     ["vasopressin"]),

    ("What is the cardiac arrest bolus dose of vasopressin?",
     "40 units IV push.",
     ["vasopressin"]),

    ("What is terlipressin?",
     "Synthetic vasopressin analog; increased V1 selectivity (more vasoconstriction, fewer renal effects); used for hepatorenal syndrome.",
     ["vasopressin"]),

    ("What is desmopressin (DDAVP)?",
     "Synthetic vasopressin analog; V2-selective; longer half-life; used for platelet dysfunction and diabetes insipidus; minimal hemodynamic effects.",
     ["vasopressin"]),

    # ═══════════════════════════════════════════════════════════════════════
    # ANGIOTENSIN II
    # ═══════════════════════════════════════════════════════════════════════
    ("What is angiotensin II?",
     "Vasopressor; naturally occurring hormone (RAAS); acts on AT1 receptors to cause vasoconstriction; approved for vasodilatory shock.",
     ["angiotensin"]),

    ("What is angiotensin II's mechanism of action?",
     "AT1 receptor agonism → vasoconstriction + aldosterone production + vasopressin release + decreased renal blood flow.",
     ["angiotensin"]),

    ("What is angiotensin II's effect on SVR?",
     "Increases SVR (vasoconstriction).",
     ["angiotensin"]),

    ("What is angiotensin II's effect on cardiac output?",
     "May decrease CO if afterload increases significantly.",
     ["angiotensin"]),

    ("When is angiotensin II preferred clinically?",
     "Refractory vasodilatory shock; patients on ACE inhibitors; high catecholamine requirements.",
     ["angiotensin"]),

    ("What is angiotensin II's major adverse effect?",
     "Increased platelet aggregation → thrombotic complications.",
     ["angiotensin"]),

    ("What is the starting dose for angiotensin II?",
     "0.02 mcg/kg/min (20 ng/kg/min); max 0.08 mcg/kg/min in first 3 hours; maintenance ≤0.04 mcg/kg/min.",
     ["angiotensin"]),

    # ═══════════════════════════════════════════════════════════════════════
    # MILRINONE
    # ═══════════════════════════════════════════════════════════════════════
    ("What is milrinone?",
     "Inodilator; bipyridine phosphodiesterase III (PDE-III) inhibitor; increases cAMP → inotropy + vasodilation.",
     ["milrinone"]),

    ("What is milrinone's mechanism of action?",
     "Inhibits PDE-III → cAMP accumulation → calcium-induced calcium release → myocyte contraction + vascular smooth muscle relaxation.",
     ["milrinone"]),

    ("What receptors does milrinone bypass?",
     "Acts downstream of beta receptors; works independently of adrenergic receptors.",
     ["milrinone", "receptors"]),

    ("What is milrinone's effect on SVR?",
     "Decreases SVR (systemic vasodilation).",
     ["milrinone"]),

    ("What is milrinone's effect on pulmonary vascular resistance?",
     "Decreases PVR (pulmonary vasodilation) — useful in pulmonary hypertension.",
     ["milrinone"]),

    ("What is milrinone's effect on heart rate?",
     "Increases HR (chronotropy).",
     ["milrinone"]),

    ("What is milrinone's effect on cardiac output?",
     "Increases CO (inotropy + afterload reduction).",
     ["milrinone"]),

    ("What is milrinone's effect on preload?",
     "Decreases preload (vasodilation).",
     ["milrinone"]),

    ("What is milrinone's effect on afterload?",
     "Decreases afterload.",
     ["milrinone"]),

    ("When is milrinone preferred clinically?",
     "Cardiogenic shock with high SVR or pulmonary hypertension; beta-blocker users; down-regulated beta receptors; RV failure with high PVR.",
     ["milrinone"]),

    ("What is milrinone's major adverse effect?",
     "Hypotension (more than dobutamine); tachyarrhythmias; prolonged effect in renal failure.",
     ["milrinone"]),

    ("What is milrinone's half-life?",
     "2–4 hours; significantly prolonged in renal failure → reduce dose.",
     ["milrinone"]),

    ("What is the typical milrinone infusion dose?",
     "0.25–0.75 mcg/kg/min.",
     ["milrinone"]),

    ("What is the milrinone loading bolus and its concern?",
     "50 mcg/kg; shortens onset but causes more hypotension and tachycardia.",
     ["milrinone"]),

    ("What are milrinone weaning considerations?",
     "Long half-life requires extended monitoring after stopping; renal failure prolongs effect; taper in heart failure to avoid rebound.",
     ["milrinone"]),

    # ═══════════════════════════════════════════════════════════════════════
    # CALCIUM
    # ═══════════════════════════════════════════════════════════════════════
    ("What is calcium's role as a vasoactive agent?",
     "Positive inotrope; final common pathway for myocyte contraction; useful in hypocalcemia-related cardiogenic shock.",
     ["calcium"]),

    ("What is the difference between calcium chloride and calcium gluconate?",
     "CaCl has ~3× more elemental calcium per gram than Ca gluconate; preferred in emergencies.",
     ["calcium"]),

    ("When is calcium chloride preferred over calcium gluconate?",
     "Emergent situations (more elemental calcium); continuous infusion via central line (more caustic).",
     ["calcium"]),

    ("What is the dose of calcium chloride for cardiogenic shock?",
     "20 mg/kg bolus or 1 g ampule; followed by 20–50 mg/kg/h infusion if beneficial.",
     ["calcium"]),

    ("What is calcium's use in CCB or beta-blocker toxicity?",
     "Competitive agonism at L-type calcium channels; overcomes CCB blockade; supplemental benefit in beta-blocker toxicity.",
     ["calcium"]),

    # ═══════════════════════════════════════════════════════════════════════
    # LEVOSIMENDAN
    # ═══════════════════════════════════════════════════════════════════════
    ("What is levosimendan?",
     "Inodilator; calcium sensitizer; increases troponin C sensitivity to calcium → inotropy without increasing O2 demand; also opens K-ATP channels → vasodilation.",
     ["levosimendan"]),

    ("What is levosimendan's effect on myocardial oxygen demand compared to catecholamines?",
     "Less increase in O2 demand (calcium sensitization vs. increased calcium influx).",
     ["levosimendan"]),

    ("When is levosimendan used clinically?",
     "Acute heart failure exacerbations (approved outside USA); diastolic dysfunction.",
     ["levosimendan"]),

    ("What is levosimendan's major adverse effect?",
     "Tachycardia; hypotension; hypokalemia; prolonged effect (active metabolites, very long half-life).",
     ["levosimendan"]),

    ("What is the levosimendan infusion duration recommendation?",
     "Less than 24 hours due to prolonged active metabolites.",
     ["levosimendan"]),

    # ═══════════════════════════════════════════════════════════════════════
    # DIGOXIN
    # ═══════════════════════════════════════════════════════════════════════
    ("What is digoxin?",
     "Cardiac glycoside; Na/K-ATPase inhibitor → increased intracellular Ca → weak inotropy; AV nodal blocker (rate control); used in atrial fibrillation.",
     ["digoxin"]),

    ("What is digoxin's mechanism of action?",
     "Inhibits Na/K-ATPase → increased intracellular Na → decreased Na/Ca exchange → increased intracellular Ca → weak inotropy.",
     ["digoxin"]),

    ("Why is digoxin used in shock with atrial fibrillation?",
     "Provides rate control without the negative inotropic effects of other rate-control agents (beta-blockers, CCBs).",
     ["digoxin"]),

    ("What is the typical digoxin bolus dose for rate control?",
     "500 mcg IV, repeated once or twice over 24 hours; adjust maintenance for renal function.",
     ["digoxin"]),

    # ═══════════════════════════════════════════════════════════════════════
    # INSULIN (HIGH-DOSE)
    # ═══════════════════════════════════════════════════════════════════════
    ("What is high-dose insulin therapy in shock?",
     "Inotrope; shifts myocardial metabolism from free fatty acids to carbohydrates → increased contractility; not catecholamine-mediated.",
     ["insulin"]),

    ("When is high-dose insulin therapy indicated?",
     "Beta-blocker toxicity; calcium channel blocker toxicity; refractory cardiogenic shock.",
     ["insulin"]),

    ("What is the high-dose insulin bolus and infusion dose?",
     "0.5–1 unit/kg bolus; then 0.5–1 unit/kg/h infusion.",
     ["insulin"]),

    ("What must accompany high-dose insulin therapy?",
     "Glucose: 0.5 g/kg bolus then 0.5–1 g/kg/h infusion (HIG therapy); also consider potassium supplementation (GIK therapy).",
     ["insulin"]),

    ("What is HIG therapy?",
     "High-dose Insulin/Glucose therapy for refractory cardiogenic shock or CCB/beta-blocker toxicity.",
     ["insulin"]),

    # ═══════════════════════════════════════════════════════════════════════
    # GLUCAGON
    # ═══════════════════════════════════════════════════════════════════════
    ("What is glucagon as a vasoactive agent?",
     "Inotrope/Chronotrope; polypeptide hormone; increases intracellular cAMP independent of beta receptors → downstream inotropy/chronotropy.",
     ["glucagon"]),

    ("What is glucagon's mechanism of action in shock?",
     "Increases intracellular cAMP → inotropy and chronotropy downstream of the beta receptor.",
     ["glucagon"]),

    ("When is glucagon preferred clinically?",
     "Beta-blocker toxicity (bypasses blocked beta receptor); verapamil/diltiazem toxicity.",
     ["glucagon"]),

    ("What is the dose of glucagon for toxicity?",
     "1–10 mg bolus; 25–75 mcg/min infusion for sustained effect.",
     ["glucagon"]),

    ("What are glucagon's adverse effects?",
     "Nausea; vomiting; hyperglycemia.",
     ["glucagon"]),

    # ═══════════════════════════════════════════════════════════════════════
    # METHYLENE BLUE
    # ═══════════════════════════════════════════════════════════════════════
    ("What is methylene blue?",
     "Vasopressor adjunct; inhibits nitric oxide synthase and soluble guanylate cyclase → decreases NO-mediated vasodilation; used for refractory vasoplegia.",
     ["methylene_blue"]),

    ("What is methylene blue's mechanism of action?",
     "Inhibits nitric oxide synthase and soluble guanylate cyclase → reduces NO → vasoconstriction.",
     ["methylene_blue"]),

    ("When is methylene blue preferred clinically?",
     "Refractory distributive shock (vasoplegia); post-cardiopulmonary bypass vasodilation.",
     ["methylene_blue"]),

    ("What is the most notable risk of methylene blue?",
     "Serotonin syndrome (especially with SSRIs or MAOIs).",
     ["methylene_blue"]),

    ("Who should avoid methylene blue?",
     "Patients on SSRIs/MAOIs (serotonin syndrome risk); G6PD deficiency (hemolysis risk).",
     ["methylene_blue"]),

    ("What is the dose of methylene blue?",
     "1.5–2.5 mg/kg IV; may follow with 0.25–0.5 mg/kg/h for 4–6 hours.",
     ["methylene_blue"]),

    # ═══════════════════════════════════════════════════════════════════════
    # HYDROXOCOBALAMIN
    # ═══════════════════════════════════════════════════════════════════════
    ("What is hydroxocobalamin?",
     "Vasopressor adjunct (vitamin B12); inhibits nitric oxide synthase → vasoconstriction; approved for cyanide poisoning; also treats vasoplegia.",
     ["hydroxocobalamin"]),

    ("What is hydroxocobalamin's mechanism of action in vasoplegia?",
     "Inhibits nitric oxide synthase → reduces NO → vasoconstriction.",
     ["hydroxocobalamin"]),

    ("What advantages does hydroxocobalamin have over methylene blue?",
     "No risk of serotonin syndrome; no hemolysis risk.",
     ["hydroxocobalamin"]),

    ("What are hydroxocobalamin's major adverse effects?",
     "Expensive; interferes with lab tests (Hgb, creatinine, coagulation studies); interferes with hemodialysis dialysate sensors.",
     ["hydroxocobalamin"]),

    ("What is the dose of hydroxocobalamin for vasoplegia?",
     "5 or 10 g IV over 15 minutes; can be repeated.",
     ["hydroxocobalamin"]),

    # ═══════════════════════════════════════════════════════════════════════
    # STEROIDS
    # ═══════════════════════════════════════════════════════════════════════
    ("What role do glucocorticoids play in vasopressor therapy?",
     "Direct vasoconstricting effect; increase catecholamine receptor responsiveness; blunt nitric oxide vasodilation.",
     ["steroids", "hydrocortisone"]),

    ("When are steroids indicated in shock?",
     "Suspected adrenal insufficiency; refractory septic/vasodilatory shock not responsive to vasopressors.",
     ["steroids"]),

    ("What is the standard hydrocortisone dose for shock?",
     "200 mg/day in divided doses or continuous infusion; typically 7-day course with taper.",
     ["steroids", "hydrocortisone"]),

    ("Why is hydrocortisone the preferred steroid in shock?",
     "Provides both glucocorticoid and mineralocorticoid effects; short-intermediate acting.",
     ["steroids", "hydrocortisone"]),

    ("Which steroid has the highest anti-inflammatory potency?",
     "Betamethasone and dexamethasone (20–30× relative to hydrocortisone); long-acting (36–54h biologic half-life).",
     ["steroids"]),

    ("Which steroids have no mineralocorticoid activity?",
     "Methylprednisolone, triamcinolone, betamethasone, dexamethasone.",
     ["steroids"]),

    # ═══════════════════════════════════════════════════════════════════════
    # ATROPINE
    # ═══════════════════════════════════════════════════════════════════════
    ("What is atropine?",
     "Parasympatholytic; muscarinic antagonist; belladonna alkaloid; increases HR by blocking vagal tone.",
     ["atropine"]),

    ("What is atropine's mechanism of action?",
     "Muscarinic (cholinergic) antagonist → blocks vagal tone → increases HR.",
     ["atropine"]),

    ("When is atropine used clinically?",
     "Symptomatic bradycardia from excess parasympathetic stimulation; procedural (ET suctioning, turning).",
     ["atropine"]),

    ("What is the typical atropine dose for bradycardia?",
     "0.5–1 mg IV bolus; duration ~30–60 minutes; may repeat.",
     ["atropine"]),

    ("What is the paradoxical effect of low-dose atropine?",
     "Very low doses may cause paradoxical decrease in HR (central vagal response).",
     ["atropine"]),

    ("What is a contraindication to atropine?",
     "Heart transplant patients (risk of prolonged heart block due to denervated heart).",
     ["atropine"]),

    ("What are atropine's adverse effects?",
     "Tachydysrhythmias; vision changes; dry mouth; mental status changes (especially elderly).",
     ["atropine"]),

    # ═══════════════════════════════════════════════════════════════════════
    # GLYCOPYRROLATE
    # ═══════════════════════════════════════════════════════════════════════
    ("What is glycopyrrolate?",
     "Parasympatholytic; synthetic atropine derivative; does NOT cross the blood-brain barrier → no CNS effects; longer duration than atropine.",
     ["glycopyrrolate"]),

    ("What is the advantage of glycopyrrolate over atropine?",
     "Does not cross the blood-brain barrier → no mental status changes; longer duration (2–3 hours).",
     ["glycopyrrolate"]),

    ("What is the typical glycopyrrolate dose?",
     "0.1–0.4 mg IV bolus; titrate to effect; lasts 2–3 hours.",
     ["glycopyrrolate"]),

    # ═══════════════════════════════════════════════════════════════════════
    # SPECIAL CLINICAL SITUATIONS
    # ═══════════════════════════════════════════════════════════════════════

    # Cardiogenic shock
    ("What is cardiogenic shock?",
     "Inadequate perfusion due to failure of the heart to pump effectively; low CO, high SVR.",
     ["shock"]),

    ("What formula describes cardiac output?",
     "CO = Stroke Volume × Heart Rate.",
     ["physiology", "shock"]),

    ("What is the first-line inotrope for cardiogenic shock?",
     "Dobutamine.",
     ["shock", "dobutamine"]),

    ("When is milrinone preferred over dobutamine in cardiogenic shock?",
     "High SVR; pulmonary hypertension; patient on beta-blockers or beta-agonists; down-regulated beta receptors.",
     ["shock", "milrinone"]),

    ("When is epinephrine preferred in cardiogenic shock?",
     "Low blood pressure with need for combined inopressor effect.",
     ["shock", "epi"]),

    # Distributive shock
    ("What is the preferred vasopressor for undifferentiated shock?",
     "Norepinephrine.",
     ["shock", "norepi"]),

    ("What is the advantage of vasopressin over catecholamines in distributive shock with acidosis?",
     "Vasopressin is equally efficacious at low pH; catecholamine receptors are impaired in acidosis.",
     ["shock", "vasopressin"]),

    # RV failure
    ("What vasopressor is preferred in RV failure?",
     "Vasopressin (maintains systemic BP without raising pulmonary vascular resistance).",
     ["shock", "vasopressin"]),

    ("Why is phenylephrine avoided in RV failure?",
     "Increases RV afterload (pulmonary vasoconstriction) and provides no inotropy.",
     ["shock", "phenylephrine"]),

    ("What are causes of increased RV afterload in ICU patients?",
     "Volume overload; hypoxemia; hypercarbia; acidosis; positive pressure ventilation; left-sided heart failure.",
     ["shock"]),

    ("What is ventricular interdependence?",
     "Increased RV pressure shifts the interventricular septum leftward → impairs LV filling and stroke volume.",
     ["physiology", "shock"]),

    # Valvular disease
    ("In aortic stenosis, what hemodynamic targets are preferred?",
     "Lower heart rate (slower = more fill time); higher afterload (vasopressors like phenylephrine or vasopressin); avoid inotropy/chronotropy.",
     ["shock"]),

    ("In valvular regurgitation, what hemodynamic targets are preferred?",
     "Higher heart rate (less time for regurgitation); lower afterload (inodilators like milrinone/dobutamine).",
     ["shock"]),

    ("Why are chronotropic agents avoided in mitral or aortic stenosis?",
     "Tachycardia reduces filling time across the stenotic valve → worse hemodynamics.",
     ["shock"]),

    # Diastolic dysfunction
    ("What is diastolic dysfunction?",
     "Impaired myocardial relaxation; may coexist with normal or reduced ejection fraction.",
     ["physiology"]),

    ("Why is tachycardia harmful in diastolic dysfunction?",
     "Reduced diastolic filling time worsens cardiac output.",
     ["physiology"]),

    ("How does positive pressure ventilation help diastolic dysfunction?",
     "Decreases preload and afterload; improves oxygenation; reduces work of breathing.",
     ["physiology"]),

    # Toxic overdose
    ("What is the treatment for calcium channel blocker (non-DHP) toxicity?",
     "Calcium chloride (competitive agonism); glucagon (bypasses receptor); high-dose insulin/glucose; epinephrine; mechanical circulatory support if refractory.",
     ["toxicology"]),

    ("What is the treatment for beta-blocker toxicity?",
     "Glucagon (bypasses beta receptor); calcium; beta-agonists (isoproterenol, dobutamine, epi); high-dose insulin/glucose; lipid emulsion; mechanical support if refractory.",
     ["toxicology"]),

    ("How does glucagon treat beta-blocker toxicity?",
     "Increases cAMP via a receptor independent of beta receptors → restores inotropy/chronotropy.",
     ["toxicology", "glucagon"]),

    ("Why is high-dose insulin effective in CCB and beta-blocker toxicity?",
     "Mechanism is non-catecholamine-mediated; shifts myocardial metabolism to carbohydrates.",
     ["toxicology", "insulin"]),

    # Mechanical circulatory support
    ("What is an intra-aortic balloon pump (IABP)?",
     "Mechanical circulatory support; expands during diastole → augments diastolic pressure and coronary perfusion; ~1–2 L/min augmentation.",
     ["mechanical_support"]),

    ("What is VA-ECMO?",
     "Venoarterial extracorporeal membrane oxygenation; biventricular support + oxygenation; highest flow rates among mechanical support devices.",
     ["mechanical_support"]),

    ("When is mechanical circulatory support indicated in cardiogenic shock?",
     "Reversible cause present (coronary occlusion, toxic overdose) as bridge to recovery or transplant.",
     ["mechanical_support"]),

    # Administration
    ("What is the preferred route for vasopressor infusions?",
     "Central venous catheter (reduces extravasation risk); peripheral IV acceptable short-term at low doses.",
     ["administration"]),

    ("Which vasopressors are safer to give peripherally?",
     "Phenylephrine and epinephrine (tolerated subcutaneously); norepinephrine and dopamine carry extravasation risk.",
     ["administration"]),

    ("What is a push-dose pressor?",
     "Diluted vasoactive bolus (e.g., epinephrine 10 mcg/mL or phenylephrine 100 mcg/mL) given as 1–2 mL IV boluses for immediate BP support.",
     ["administration"]),

    # Approach to undifferentiated hypotension
    ("What is the first step in approaching undifferentiated hypotension?",
     "Assess cardiac pump function (point-of-care echo): dysrhythmia? systolic dysfunction? valvular abnormality?",
     ["shock"]),

    ("In undifferentiated hypotension with normal heart and low preload, what is the treatment?",
     "Volume resuscitation (hypovolemic shock).",
     ["shock"]),

    ("In undifferentiated hypotension with normal heart and adequate preload, what is the treatment?",
     "Vasopressor (distributive shock).",
     ["shock"]),

    # Drug comparisons
    ("How does dobutamine differ from milrinone mechanistically?",
     "Dobutamine: beta-1 agonist (receptor-dependent); Milrinone: PDE-III inhibitor (receptor-independent, bypasses beta receptors).",
     ["dobutamine", "milrinone"]),

    ("Compare norepinephrine vs phenylephrine in distributive shock.",
     "Norepi: alpha-1 dominant + mild beta-1 inotropy → preferred (maintains CO); Phenylephrine: pure alpha-1 → may decrease CO.",
     ["norepi", "phenylephrine"]),

    ("What is the main difference between vasopressin and catecholamines in shock?",
     "Vasopressin: pH-insensitive, no pulmonary vasoconstriction; catecholamines: impaired in acidosis, may increase PVR.",
     ["vasopressin"]),

    ("Compare methylene blue vs hydroxocobalamin for vasoplegia.",
     "Both inhibit NO synthase; MB: cheaper but risks serotonin syndrome/hemolysis (G6PD); Hydroxocobalamin: safer but expensive, interferes with labs.",
     ["methylene_blue", "hydroxocobalamin"]),
]

# ── Build deck ───────────────────────────────────────────────────────────────
deck = genanki.Deck(DECK_ID, DECK_NAME)

seen_questions = set()
skipped = 0
notes_added = 0

for entry in RAW_CARDS:
    question, answer, extra_tags = entry
    q_key = question.strip().lower()
    if q_key in seen_questions:
        skipped += 1
        continue
    seen_questions.add(q_key)

    tags = ["ccrn::pharmacology"] + [f"ccrn::{t}" for t in extra_tags]

    note = genanki.Note(
        model=model,
        fields=[question, answer, " ".join(tags)],
        tags=tags,
    )
    deck.add_note(note)
    notes_added += 1

# ── Write TSV ────────────────────────────────────────────────────────────────
tsv_path = "/home/user/ccrncards/ccrn_inotropes_cards.tsv"
with open(tsv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["Question", "Answer", "Tags"])
    for note in deck.notes:
        writer.writerow([note.fields[0], note.fields[1], " ".join(note.tags)])

# ── Write APKG ───────────────────────────────────────────────────────────────
apkg_path = "/home/user/ccrncards/CCRN - Inotropes & Vasopressors (ICU Masterclass).apkg"
package = genanki.Package(deck)
package.write_to_file(apkg_path)

# ── Report ───────────────────────────────────────────────────────────────────
print(f"Cards written  : {notes_added}")
print(f"Duplicates skipped: {skipped}")
print(f"TSV  : {tsv_path}")
print(f"APKG : {apkg_path}")

tsv_size  = os.path.getsize(tsv_path)
apkg_size = os.path.getsize(apkg_path)
print(f"TSV  size: {tsv_size:,} bytes")
print(f"APKG size: {apkg_size:,} bytes")
print("Done.")
