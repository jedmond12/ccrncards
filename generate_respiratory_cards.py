#!/usr/bin/env python3
import csv
import random

# Read the extracted text
with open("extracted/respiratory_chapter.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Define comprehensive cards based on the chapter content
cards = []

# VENTILATION
cards.append(("What is ventilation?", "Movement of air in and out to maintain O2 and CO2 concentrations"))
cards.append(("What is primary control of ventilation?", "Central control (brain stem) senses blood pH"))
cards.append(("What stimulates ventilation?", "Decreased pH (acidosis)"))
cards.append(("What is secondary control of ventilation?", "Peripheral control (aortic arch) senses PaO2"))
cards.append(("What stimulates peripheral ventilation control?", "Decreased PaO2 (hypoxemia)"))
cards.append(("What do chronic PaCO2 retainers rely on?", "Mild hypoxemia for ventilator drive"))
cards.append(("What is clinical indicator of ventilation?", "PaCO2 (NOT PaO2)"))
cards.append(("What is minute ventilation?", "Tidal volume × respiratory rate"))
cards.append(("What is normal minute ventilation?", "~4 L/minute"))
cards.append(("What does increased minute ventilation indicate?", "Increased work of breathing"))
cards.append(("What is primary muscle of ventilation?", "Diaphragm"))
cards.append(("What affects diaphragm function?", "Deconditioning, hypoxemia, acidosis, hypophosphatemia"))
cards.append(("What is optimal position for ventilation?", "Upright sitting position"))
cards.append(("What is worst position for respiratory distress?", "Supine (flat on back)"))

# DEAD SPACE VENTILATION
cards.append(("What is dead space ventilation?", "Volume of air that does not participate in gas exchange"))
cards.append(("What is anatomic dead space?", "~2 mL/kg Vt; nose down to alveoli"))
cards.append(("What is alveolar dead space?", "Pathologic, non-perfused alveoli (e.g., PE)"))
cards.append(("What is physiological dead space?", "Anatomic dead space + alveolar dead space"))
cards.append(("What increases alveolar dead space?", "Pulmonary embolus"))

# PULMONARY PERFUSION
cards.append(("What is pulmonary perfusion?", "Movement of blood through pulmonary capillaries"))
cards.append(("What is normal V/Q ratio?", "0.8 (ideal lung unit)"))
cards.append(("What decreases pulmonary perfusion?", "PE, low cardiac output"))
cards.append(("What is clinical implication of gravity on perfusion?", "Good lung down"))
cards.append(("Why avoid turning patient to bad lung?", "More blood goes to bad lung, may worsen hypoxemia"))
cards.append(("What explains improved oxygenation with prone positioning?", "Perfusion of under-perfused anterior chest alveoli"))

# V/Q RATIO
cards.append(("What happens with normal V/Q ratio?", "Normal gas exchange on room air"))
cards.append(("What is V/Q mismatch?", "Problem with ventilation or perfusion causing hypoxemia"))
cards.append(("How to treat V/Q mismatch?", "Give O2, identify and treat underlying problem"))
cards.append(("What is a shunt?", "Extreme V/Q mismatch; 100% FiO2 does NOT correct hypoxemia"))
cards.append(("What is pathologic shunt?", "ARDS; blood goes through lungs but does NOT get oxygenated"))
cards.append(("What is treatment for shunt?", "Oxygen AND PEEP"))
cards.append(("What does PEEP do?", "Decreases surface tension, increases alveolar recruitment, increases driving pressure"))

# OXYGENATION ASSESSMENT
cards.append(("What is required for adequate oxygenation?", "Adequate ventilation, O2 transfer, hemoglobin, cardiac output, O2 release, cell O2 utilization"))
cards.append(("What happens without sufficient oxygen at cellular level?", "Lactic acidosis (anaerobic metabolism)"))
cards.append(("What is goal SpO2 for critically ill?", "≥ 90%"))
cards.append(("What PaO2 correlates with SpO2 < 90%?", "< 60 mmHg"))

# OXYHEMOGLOBIN-DISSOCIATION CURVE
cards.append(("What shifts oxyhemoglobin curve to LEFT?", "Hemoglobin holds onto O2; alkalosis, hypothermia, decreased 2,3-DPG"))
cards.append(("What shifts oxyhemoglobin curve to RIGHT?", "Hemoglobin releases O2; acidosis, fever, increased 2,3-DPG"))
cards.append(("What is 2,3-DPG?", "Organic phosphate in RBCs that alters Hgb affinity for O2"))
cards.append(("What does decreased 2,3-DPG cause?", "Hemoglobin holds onto O2"))
cards.append(("What does increased 2,3-DPG cause?", "Hemoglobin releases O2 more readily"))

# CARBON MONOXIDE POISONING
cards.append(("What is CO affinity for Hgb vs O2?", "~230 times greater"))
cards.append(("Why not use pulse oximetry for CO poisoning?", "Cannot differentiate between CO and O2"))
cards.append(("What is treatment for CO poisoning?", "100% FiO2 until symptoms resolve and COHb < 10%"))
cards.append(("When to use hyperbaric oxygen for CO?", "If available within 30 minutes"))

# LUNG COMPLIANCE
cards.append(("What is compliance?", "Degree of elasticity of tissue"))
cards.append(("What does decreased compliance cause?", "Increased resistance or stiffness"))
cards.append(("What is static compliance?", "Elastic properties of lung"))
cards.append(("What is dynamic compliance?", "Elastic properties of airways"))
cards.append(("What is normal compliance?", "~45-50 mL/cm H2O"))
cards.append(("What compliance is affected in asthma?", "Dynamic compliance decreased; static normal"))
cards.append(("What compliance is affected in ARDS?", "Static and dynamic compliance both decreased"))
cards.append(("What does decreased compliance do to work of breathing?", "Increases work of breathing"))

# ACID-BASE BASICS
cards.append(("What does pH represent?", "Hydrogen ion (H+) concentration"))
cards.append(("What is relationship between H+ and pH?", "Inverse; increased H+ = decreased pH"))
cards.append(("What is PaCO2?", "Acid; respiratory parameter controlled by lungs"))
cards.append(("How quickly can lungs change PaCO2?", "Within minutes (rapid)"))
cards.append(("What is HCO3?", "Base; metabolic parameter controlled by kidneys"))
cards.append(("How quickly can kidneys change HCO3?", "Hours to days (slow)"))
cards.append(("What is normal pH?", "7.35-7.45"))
cards.append(("What is normal PaCO2?", "35-45 mmHg"))
cards.append(("What is normal HCO3?", "22-26 mEq/L"))

# ACID-BASE DISORDERS
cards.append(("What is respiratory acidosis?", "pH < 7.35, PaCO2 > 45"))
cards.append(("What is respiratory alkalosis?", "pH > 7.45, PaCO2 < 35"))
cards.append(("What is metabolic acidosis?", "pH < 7.35, HCO3 < 22"))
cards.append(("What is metabolic alkalosis?", "pH > 7.45, HCO3 > 26"))

# ANION GAP
cards.append(("What is normal anion gap?", "5-15 mEq/L"))
cards.append(("What does anion gap help determine?", "Cause of and response to treatment for metabolic acidosis"))

# ACUTE RESPIRATORY FAILURE
cards.append(("What is acute respiratory failure?", "PaO2 ≤ 60 mmHg with or without PaCO2 ≥ 50 mmHg with pH < 7.30"))
cards.append(("What is Type 1 respiratory failure?", "Hypoxemic (e.g., ARDS, pneumonia, PE)"))
cards.append(("What is Type 2 respiratory failure?", "Hypercapnic (e.g., COPD, CNS depression, sleep apnea)"))
cards.append(("What is Type 3 respiratory failure?", "Both hypoxemic and hypercapnic (e.g., late ARDS, late COPD)"))
cards.append(("What are signs of hypoxemic respiratory failure?", "Tachypnea, adventitious breath sounds, accessory muscle use, tachyarrhythmias, cyanosis, anxiety"))
cards.append(("What are signs of hypercapnic respiratory failure?", "Shallow breathing, bradypnea, decreased LOC"))

# TREATMENT OF ACUTE RESPIRATORY FAILURE
cards.append(("What is treatment for acute respiratory failure?", "Maintain airway, improve ventilation, optimize oxygenation, optimize circulation, identify etiology"))
cards.append(("What FiO2 goal in acute respiratory failure?", "SaO2 > 0.90"))
cards.append(("When to decrease FiO2?", "To ≤ 0.50 ASAP"))

# NIV
cards.append(("What is CPAP?", "Continuous positive airway pressure"))
cards.append(("What is CPAP indicated for?", "Hypoxemic respiratory failure with increased work of breathing"))
cards.append(("What are CPAP settings?", "FiO2 and 1 pressure setting"))
cards.append(("What is BiPAP?", "Bilevel positive airway pressure"))
cards.append(("What is BiPAP indicated for?", "Hypoxemic and/or hypercapnic respiratory failure"))
cards.append(("What are BiPAP settings?", "FiO2, IPAP, and EPAP"))
cards.append(("What does IPAP assist?", "Ventilation"))
cards.append(("What does EPAP assist?", "Oxygenation"))
cards.append(("What are contraindications for NIV?", "Hemodynamic instability, copious secretions, high aspiration risk, impaired mental status, suspected pneumothorax, inability to cooperate, life-threatening refractory hypoxemia"))

# HFNC
cards.append(("What is HFNC?", "High-flow nasal cannula oxygen therapy"))
cards.append(("What can HFNC deliver?", "FiO2 up to 100% at flow rates up to 60 L/min"))
cards.append(("What are advantages of HFNC?", "High FiO2, heated/humidified, meets high flow demands, decreases dead space"))
cards.append(("What are limitations of HFNC?", "Cannot deliver higher airway pressures, limited pressure support for hypercapnia"))

# COPD
cards.append(("What does COPD include?", "Emphysema, asthma, bronchitis"))
cards.append(("What is easier in COPD?", "Inspiration easier than exhalation"))
cards.append(("What are consequences of COPD?", "Dynamic hyperinflation, air trapping, auto-PEEP, low expiratory flow rates"))
cards.append(("What causes V/Q mismatch in COPD?", "Problem with ventilation, increased PaCO2"))
cards.append(("What is cor pulmonale?", "Right ventricular enlargement from COPD"))
cards.append(("What are signs of acute COPD exacerbation?", "Worsening dyspnea, increased sputum purulence/volume, hypercapnia, hypoxemia"))
cards.append(("What is treatment for acute COPD exacerbation?", "Titrate FiO2 to SaO2 > 90%, bronchodilators, corticosteroids, antibiotics if pneumonia, NIV or intubation if needed"))

# STATUS ASTHMATICUS
cards.append(("What is status asthmaticus?", "Severe airway narrowing refractory to aggressive bronchodilator therapy"))
cards.append(("What are signs of status asthmaticus?", "Dyspnea, tachypnea, accessory muscle use, wheezing → decreased → absent breath sounds, pulsus paradoxus ≥ 15 mmHg"))
cards.append(("What is ominous sign in status asthmaticus?", "Absent breath sounds (silent chest)"))
cards.append(("What is normal peak flow rate?", "> 80% of predicted"))
cards.append(("What peak flow rate is severe?", "< 50%"))
cards.append(("When to admit to ICU for asthma?", "Peak flow rate < 50%"))
cards.append(("What is treatment for status asthmaticus?", "Short-acting beta-2 agonists, anticholinergics, systemic corticosteroids, O2, hydration, avoid sedation"))
cards.append(("When to intubate for status asthmaticus?", "Respiratory acidosis, severe hypoxemia, silent chest, decreased LOC"))
cards.append(("What ventilator settings for status asthmaticus?", "Low rate, low tidal volumes, increased I:E ratio (> 1:3-4)"))
cards.append(("Why avoid paralytics in status asthmaticus?", "Combined with steroids increases neuropathy"))

# PULMONARY EMBOLISM
cards.append(("What is pulmonary embolism?", "Partial or complete obstruction of pulmonary capillary bed by clot"))
cards.append(("What is massive PE?", "> 50% occlusion"))
cards.append(("What is submassive PE?", "< 50% occlusion"))
cards.append(("What percent of PE result from DVT?", "80-90%"))
cards.append(("What does PE increase?", "Alveolar dead space"))
cards.append(("What are signs/symptoms of PE?", "Dyspnea, tachypnea, chest pain, tachycardia, hypoxemia, anxiety, hemoptysis"))
cards.append(("What is gold standard for PE diagnosis?", "Pulmonary angiography"))
cards.append(("What is D-dimer?", "Good rule-out test; positive means clot present in body"))
cards.append(("What prevents PE?", "Early mobilization, SCDs, anticoagulation (heparin, enoxaparin)"))
cards.append(("What is treatment for PE?", "Maintain airway/ventilation/oxygenation, fluids, anticoagulation (heparin, LMWH, Coumadin)"))
cards.append(("When to use fibrinolytic therapy for PE?", "Hemodynamic compromise with low bleeding risk"))

# PULMONARY HYPERTENSION
cards.append(("What is pulmonary hypertension?", "Mean PA pressure > 25 mmHg at rest with PAOP < 16 mmHg"))
cards.append(("What is normal mean PA pressure?", "~20 mmHg"))
cards.append(("What does PH cause?", "Cor pulmonale and right ventricular failure"))
cards.append(("What are signs/symptoms of PH?", "Exertional dyspnea, lethargy, fatigue, RV failure, chest pain, syncope, peripheral edema"))
cards.append(("What is treatment for PH?", "Treat underlying cause, diuretics, oxygen, anticoagulants, digoxin, dilators"))
cards.append(("What dilators for PH?", "Calcium channel blockers, phosphodiesterase-5 inhibitors (sildenafil, tadalafil)"))

# PNEUMONIA
cards.append(("What is pneumonia?", "Acute inflammation of lung parenchyma from infectious agent"))
cards.append(("What causes pneumonia?", "Bacterial, viral, fungal, parasitic"))
cards.append(("What is community-acquired pneumonia?", "Outside hospital; common pathogen: Streptococcus pneumoniae"))
cards.append(("What is hospital-acquired pneumonia?", "≥ 48 hours after admission; common pathogen: Pseudomonas aeruginosa"))
cards.append(("What is ventilator-associated pneumonia?", "≥ 48 hours after intubation"))
cards.append(("What are risk factors for pneumonia?", "Age, COPD, smoking, decreased LOC, artificial airways, chronic illness, malnutrition, immunocompromised"))
cards.append(("What are signs/symptoms of pneumonia?", "Fever, chills, productive cough, tachycardia, chest pain, confusion, accessory muscle use"))
cards.append(("What are auscultation findings over pneumonia consolidation?", "Increased tactile fremitus, dull to percussion, bronchial breath sounds, bronchophony, egophony, whispered pectoriloquy"))
cards.append(("What is treatment for pneumonia?", "Optimize oxygenation/ventilation, position GOOD lung DOWN, bronchial hygiene, identify organism, antibiotic therapy"))
cards.append(("When to give first antibiotic dose for pneumonia?", "Within 4 hours if presenting to ED"))
cards.append(("What prevents hospital-acquired pneumonia?", "Hand hygiene, HOB ≥ 30°, feed patient, oral hygiene"))
cards.append(("What prevents VAP?", "All HAP prevention PLUS drain condensate, change tubing when contaminated, mobilize, aseptic suctioning, chlorhexidine mouth rinse, brush teeth, keep ETT cuff inflated"))

# ASPIRATION
cards.append(("What is aspiration?", "Inhalation of toxic substances into lung with injury"))
cards.append(("What is most common type of aspiration?", "Oropharyngeal"))
cards.append(("Where do most aspirations occur?", "RIGHT lung (due to anatomy)"))
cards.append(("What are causes of aspiration?", "Altered LOC, drug/alcohol abuse, depressed gag/cough/swallow, feeding tubes, improper positioning, artificial airways"))
cards.append(("What are signs of aspiration?", "Acute respiratory distress, gastric contents in oropharynx, tachycardia, hypoxemia, crackles, copious secretions, hypotension"))

# ARDS/ALI
cards.append(("What is ARDS?", "Inflammatory response causing increased pulmonary capillary permeability with proteinaceous fluid in alveoli"))
cards.append(("What is ARDS also called?", "Noncardiogenic pulmonary edema"))
cards.append(("What cells are damaged in ARDS?", "Type II alveolar cells (produce surfactant)"))
cards.append(("What does surfactant do?", "Stabilizes alveoli, keeps them open, increases compliance, eases work of breathing"))
cards.append(("What happens without surfactant?", "Massive atelectasis, decreased compliance, increased work of breathing, decreased FRC"))
cards.append(("What is ARDS criteria?", "Bilateral infiltrates, PAOP < 18, refractory hypoxemia, PaO2/FiO2 < 200"))
cards.append(("What is ALI criteria?", "Same as ARDS but PaO2/FiO2 200-300"))
cards.append(("What are ARDS etiologies?", "Sepsis, aspiration, pneumonia, trauma, pancreatitis, shock, near-drowning, drug overdose, massive transfusion"))
cards.append(("What are signs/symptoms of ARDS?", "Severe dyspnea, tachypnea, refractory hypoxemia, decreased compliance, crackles, cyanosis"))
cards.append(("What is treatment for ARDS?", "Intubation, mechanical ventilation, PEEP ≥ 15, limit plateau pressure ≤ 30, limit Vt 5-6 mL/kg, prone positioning, support BP, DVT prophylaxis, stress ulcer prophylaxis"))
cards.append(("What is permissive hypercapnia?", "Low Vt causes rise in PaCO2, drop in pH; tolerate pH as low as 7.2 to prevent volutrauma"))
cards.append(("What happens if ventilator disconnected in ARDS?", "Alveolar derecruitment and hypoxemia that may not be readily corrected"))
cards.append(("What is mortality from ARDS?", "~30%"))
cards.append(("What do ARDS patients die from?", "MODS, not hypoxemia"))
cards.append(("What are ARDS complications?", "Secondary infections, PE, ileus, skin breakdown, malnutrition, barotrauma"))
cards.append(("Are steroids used for ARDS?", "No (except select COVID-19 pneumonia)"))

# PNEUMOTHORAX
cards.append(("What is pneumothorax?", "Air in pleural space"))
cards.append(("What are types of pneumothorax?", "Spontaneous, traumatic (open/closed), iatrogenic, tension"))
cards.append(("What is tension pneumothorax?", "Air unable to exit → mediastinal shift → life-threatening"))
cards.append(("What are signs of pneumothorax?", "Sudden chest pain, dyspnea, tachypnea, decreased/absent breath sounds, hyperresonance, hypoxemia"))
cards.append(("What are signs of tension pneumothorax?", "Hypotension, tracheal deviation to opposite side, severe respiratory distress, JVD"))
cards.append(("What is treatment for pneumothorax > 20%?", "Chest tube, supplemental O2, pain treatment"))
cards.append(("What is treatment for pneumothorax < 20%?", "O2, monitor for lung reexpansion"))

# CHEST TUBE MANAGEMENT
cards.append(("What should water seal chamber show?", "Tidaling with deep inspiration (normal)"))
cards.append(("What does bubbling in water seal chamber indicate?", "Air leak (NOT normal)"))
cards.append(("What determines suction amount in chest tube?", "Gauge or water level, NOT wall suction source"))
cards.append(("When to clamp chest tube?", "Only when changing system, with disconnection, or with physician order"))
cards.append(("Why not clamp chest tube routinely?", "Cuts off negative pressure; lung may re-collapse"))

# MECHANICAL VENTILATION
cards.append(("How to confirm ETT placement?", "Waveform capnography (most accurate), end-tidal CO2, auscultation"))
cards.append(("What is ETT cuff pressure?", "20 cm H2O"))
cards.append(("Where should ETT be on CXR?", "3-5 cm above carina"))
cards.append(("Where does ETT migrate if it migrates?", "Right lung (shorter, wider, less angle)"))
cards.append(("When to get ABGs after intubation?", "Within 20-30 minutes"))

# VENTILATOR MODES
cards.append(("What is assist-control mode?", "Patient receives set Vt at set rate; all patient-triggered breaths get set Vt"))
cards.append(("What is SIMV mode?", "Patient receives set Vt at set rate; breaths above set rate are spontaneous at patient's own Vt"))
cards.append(("Is AC a weaning mode?", "No (unless alternated with spontaneous breathing periods)"))
cards.append(("Is SIMV a weaning mode?", "Yes (reducing rate allows patient to assume more work)"))

# VENTILATOR SETTINGS
cards.append(("What does PEEP do?", "Positive pressure applied at end of exhalation; increases FRC, increases alveolar recruitment"))
cards.append(("What is CPAP?", "PEEP applied to spontaneously breathing patient; no machine breaths"))
cards.append(("What is PSV?", "Pressure support ventilation; increases airway pressure during inspiration to boost spontaneous Vt"))
cards.append(("When is PSV triggered?", "Patient-triggered (not if paralyzed/sedated)"))
cards.append(("What is normal breath rate?", "12-16 breaths/minute"))
cards.append(("What is normal tidal volume?", "6-8 mL/kg"))
cards.append(("What is tidal volume for ARDS?", "5-6 mL/kg (to prevent volutrauma)"))
cards.append(("What FiO2 on intubation?", "100%, then adjust down to ≤ 50% ASAP"))

# VENTILATOR ALARMS
cards.append(("What causes high-pressure alarms?", "Agitation, coughing, secretions, aspiration, kinked ETT, bronchospasm, decreasing compliance, pneumothorax"))
cards.append(("What causes low-pressure alarms?", "Circuit disconnection/leak, inadequate Vt, cuff leak, chest tube leak"))
cards.append(("What to do if unable to troubleshoot alarm?", "Disconnect ventilator, ventilate with bag/valve device"))

# VENTILATOR SETTINGS FOR SPECIFIC CONDITIONS
cards.append(("What ventilator settings for ARDS?", "Low Vt (5-6 mL/kg), high PEEP (≥ 15), limit plateau pressure ≤ 30"))
cards.append(("What ventilator settings for asthma?", "Low rate, low Vt, increased I:E ratio (> 1:3-4), no PEEP"))

# WEANING
cards.append(("What are criteria for weaning?", "Original reason resolved, minute ventilation < 10 L/min, spontaneous Vt > 5 mL/kg, NIF > -25 cm H2O, RSBI < 105, vital capacity > 10 mL/kg, ABGs acceptable on FiO2 ≤ 50%"))
cards.append(("What are criteria to stop spontaneous breathing trial?", "RR > 35 or < 8, SpO2 < 88%, respiratory distress, mental status change, cardiac arrhythmia, hypotension"))

# MEDICATIONS
cards.append(("What is albuterol (Ventolin)?", "Short-acting beta-2 agonist; bronchodilator; for asthma, COPD"))
cards.append(("What is ipratropium (Atrovent)?", "Anticholinergic; bronchodilator; for asthma, COPD"))
cards.append(("What is sildenafil (Viagra)?", "Phosphodiesterase-5 inhibitor; vasodilator; for pulmonary hypertension"))
cards.append(("What is tadalafil (Cialis)?", "Phosphodiesterase-5 inhibitor; vasodilator; for pulmonary hypertension"))

print(f"Generated {len(cards)} cards")

# Remove duplicates
seen_questions = set()
unique_cards = []
for q, a in cards:
    if q not in seen_questions:
        unique_cards.append((q, a))
        seen_questions.add(q)

print(f"After deduplication: {len(unique_cards)} unique cards")

# Write to TSV
with open("ccrn_respiratory_cards.tsv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(["Question", "Answer", "Tags"])
    for question, answer in unique_cards:
        # Determine tags based on content
        tags = ["ccrn::respiratory"]

        # Add specific tags
        if any(word in question.lower() for word in ['ventilation', 'minute ventilation', 'diaphragm', 'paco2']):
            tags.append("ventilation")
        if any(word in question.lower() for word in ['dead space', 'pe', 'pulmonary embolism', 'embolus']):
            tags.append("pe")
        if any(word in question.lower() for word in ['perfusion', 'v/q', 'shunt', 'good lung']):
            tags.append("perfusion")
        if any(word in question.lower() for word in ['oxygenation', 'pao2', 'sao2', 'spo2', 'oxygen']):
            tags.append("oxygenation")
        if any(word in question.lower() for word in ['oxyhemoglobin', 'dissociation', '2,3-dpg', 'shift']):
            tags.append("oxyhemoglobin")
        if any(word in question.lower() for word in ['carbon monoxide', 'cohb', 'co poisoning']):
            tags.append("co_poisoning")
        if any(word in question.lower() for word in ['compliance', 'static', 'dynamic']):
            tags.append("compliance")
        if any(word in question.lower() for word in ['abg', 'acid', 'base', 'ph', 'hco3', 'acidosis', 'alkalosis', 'anion gap']):
            tags.append("abg")
        if any(word in question.lower() for word in ['respiratory failure', 'type 1', 'type 2', 'type 3', 'hypoxemic', 'hypercapnic']):
            tags.append("resp_failure")
        if any(word in question.lower() for word in ['niv', 'cpap', 'bipap', 'ipap', 'epap', 'noninvasive']):
            tags.append("niv")
        if any(word in question.lower() for word in ['hfnc', 'high-flow', 'nasal cannula']):
            tags.append("hfnc")
        if any(word in question.lower() for word in ['copd', 'emphysema', 'bronchitis', 'cor pulmonale', 'auto-peep']):
            tags.append("copd")
        if any(word in question.lower() for word in ['asthma', 'status asthmaticus', 'wheezing', 'peak flow', 'silent chest']):
            tags.append("asthma")
        if any(word in question.lower() for word in ['pulmonary hypertension', 'mean pa', 'cor pulmonale']):
            tags.append("pulm_htn")
        if any(word in question.lower() for word in ['pneumonia', 'cap', 'hap', 'vap', 'consolidation', 'infiltrate']):
            tags.append("pneumonia")
        if any(word in question.lower() for word in ['aspiration', 'right lung', 'oropharyngeal']):
            tags.append("aspiration")
        if any(word in question.lower() for word in ['ards', 'ali', 'surfactant', 'type ii', 'noncardiogenic', 'refractory', 'permissive']):
            tags.append("ards")
        if any(word in question.lower() for word in ['pneumothorax', 'tension', 'chest tube', 'mediastinal shift']):
            tags.append("pleural_space")
        if any(word in question.lower() for word in ['mechanical ventilation', 'ventilator', 'ett', 'intubation', 'endotracheal']):
            tags.append("vents")
        if any(word in question.lower() for word in ['mode', 'assist-control', 'ac', 'simv', 'peep', 'psv', 'pressure support']):
            tags.append("vent_modes")
        if any(word in question.lower() for word in ['alarm', 'high-pressure', 'low-pressure', 'troubleshoot']):
            tags.append("vent_alarms")
        if any(word in question.lower() for word in ['wean', 'spontaneous breathing', 'nif', 'rsbi', 'extubation']):
            tags.append("weaning")
        if any(word in (question + " " + answer).lower() for word in ['albuterol', 'ventolin', 'ipratropium', 'atrovent', 'sildenafil', 'viagra', 'tadalafil', 'cialis']):
            tags.append("meds")

        tags_str = " ".join(tags)
        writer.writerow([f"Question:\n{question}", f"Answer:\n{answer}", tags_str])

print(f"Saved {len(unique_cards)} cards to ccrn_respiratory_cards.tsv")
