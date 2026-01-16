#!/usr/bin/env python3
import csv
import random
import genanki

# Read the extracted text
with open("cardiovascular_chapter.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Define comprehensive cards based on the chapter content
cards = []

# HEART SOUNDS
cards.append(("What causes S1?", "Closure of AV valves (mitral, tricuspid)"))
cards.append(("Where is S1 loudest?", "Apex (midclavicular, 5th ICS)"))
cards.append(("What does S1 mark?", "End of diastole, beginning of systole"))
cards.append(("What causes S2?", "Closure of semilunar valves (aortic, pulmonic)"))
cards.append(("Where is S2 loudest?", "Base (right sternal border, 2nd ICS)"))
cards.append(("What does S2 mark?", "End of systole, beginning of diastole"))
cards.append(("What causes S2 splitting on inspiration?", "Normal physiologic finding; wide fixed splitting indicates RBBB"))
cards.append(("When is S2 louder?", "Pulmonary embolism"))
cards.append(("What is the aortic valve auscultatory point?", "2nd ICS, right sternal border (base)"))
cards.append(("What is the mitral valve auscultatory point?", "5th ICS, midclavicular (apex)"))
cards.append(("What causes S3?", "Rapid rush of blood into dilated ventricle"))
cards.append(("When does S3 occur?", "Early diastole, right after S2"))
cards.append(("Where is S3 best heard?", "Apex with bell of stethoscope"))
cards.append(("What is S3 associated with?", "Heart failure"))
cards.append(("What is the S3 mnemonic?", "Ventricular gallop, 'Kentucky'"))
cards.append(("What else causes S3?", "Pulmonary HTN, cor pulmonale, mitral/aortic/tricuspid insufficiency"))
cards.append(("What causes S4?", "Atrial contraction into noncompliant ventricle"))
cards.append(("When does S4 occur?", "Right before S1"))
cards.append(("Where is S4 best heard?", "Apex with bell of stethoscope"))
cards.append(("What is S4 associated with?", "MI, ischemia, HTN, ventricular hypertrophy, aortic stenosis"))
cards.append(("What is the S4 mnemonic?", "Atrial gallop, 'Tennessee'"))
cards.append(("Why is S4 not heard in atrial fibrillation?", "No atrial contraction"))
cards.append(("What causes a pericardial friction rub?", "Pericarditis"))
cards.append(("What is unique about pericardial friction rub pain?", "Worse with deep inspiration; may be positional"))

# BLOOD PRESSURE AND PULSE PRESSURE
cards.append(("What is normal pulse pressure?", "40-60 mmHg"))
cards.append(("What does systolic BP indirectly measure?", "Cardiac output and stroke volume"))
cards.append(("What does narrowing pulse pressure indicate?", "Severe hypovolemia or severe drop in CO"))
cards.append(("What is an example of narrowed pulse pressure?", "100/78"))
cards.append(("What does diastolic BP indirectly measure?", "Systemic vascular resistance (SVR)"))
cards.append(("What does widened pulse pressure indicate?", "Vasodilation, drop in SVR (seen in sepsis/septic shock)"))
cards.append(("What is an example of widened pulse pressure?", "100/38"))
cards.append(("Which phase is longer, systole or diastole?", "Diastole (one-third longer)"))
cards.append(("When are coronary arteries perfused?", "During diastole"))
cards.append(("Why do CO and BP drop with extreme tachyarrhythmias?", "No time for filling"))

# VALVULAR HEART DISEASE BASICS
cards.append(("What causes normal heart sounds S1 and S2?", "Valve closure"))
cards.append(("What determines valve opening and closing?", "Pressure gradient across valve"))
cards.append(("When does a valve open?", "When pressure above > pressure below"))
cards.append(("When does a valve close?", "When pressure below > pressure above"))
cards.append(("What is systole?", "Ejection, high pressure"))
cards.append(("What is diastole?", "Filling, low pressure"))

# CAUSES OF VALVULAR DISEASE
cards.append(("What are causes of valvular heart disease?", "CAD, ischemia, MI, dilated cardiomyopathy, degeneration, bicuspid valve, rheumatic fever, infection, connective tissue disease"))

# SYSTOLIC MURMURS
cards.append(("When do murmurs of insufficiency occur?", "When valve is closed"))
cards.append(("When do murmurs of stenosis occur?", "When valve is open"))
cards.append(("Which valves are open during systole?", "Semilunar valves (aortic, pulmonic)"))
cards.append(("Which valves are closed during systole?", "AV valves (mitral, tricuspid)"))
cards.append(("What are systolic murmurs?", "Aortic stenosis, pulmonic stenosis, mitral insufficiency, tricuspid insufficiency"))
cards.append(("Is aortic stenosis acute or chronic?", "Chronic (develops over time)"))
cards.append(("What does mitral insufficiency cause on PA catheter?", "Large V-waves on PAOP tracing"))
cards.append(("Where is VSD murmur heard?", "Left sternal border, 5th ICS"))

# DIASTOLIC MURMURS
cards.append(("Which valves are closed during diastole?", "Semilunar valves (aortic, pulmonic)"))
cards.append(("Which valves are open during diastole?", "AV valves (mitral, tricuspid)"))
cards.append(("What are diastolic murmurs?", "Aortic insufficiency, pulmonic insufficiency, mitral stenosis, tricuspid stenosis"))
cards.append(("What is mitral stenosis associated with?", "Atrial fibrillation (due to atrial enlargement)"))

# MURMURS WITH ACUTE MI
cards.append(("When does mitral insufficiency murmur occur?", "Systole (mitral valve closed)"))
cards.append(("When does mitral stenosis murmur occur?", "Diastole (mitral valve open)"))
cards.append(("When does aortic insufficiency murmur occur?", "Diastole (aortic valve closed)"))
cards.append(("When does aortic stenosis murmur occur?", "Systole (aortic valve open)"))
cards.append(("When does VSD murmur occur?", "Systole (ejection)"))
cards.append(("What causes acute mitral valve regurgitation with MI?", "Papillary muscle dysfunction or rupture"))
cards.append(("Where is papillary muscle dysfunction murmur loudest?", "Apex"))
cards.append(("What grade is papillary muscle dysfunction?", "Grade I or II"))
cards.append(("What grade is papillary muscle rupture?", "Grade V or VI"))
cards.append(("Is papillary muscle rupture a surgical emergency?", "Yes"))

# ACUTE CORONARY SYNDROME - RISK FACTORS
cards.append(("What are CAD risk factors?", "HTN, diabetes, smoking, dyslipidemia, family history, age, obesity, sedentary lifestyle"))

# ACS SPECTRUM
cards.append(("What is asymptomatic CAD?", "Silent coronary disease"))
cards.append(("What is stable angina?", "Chest pain with activity, predictable, fixed calcified lesions"))
cards.append(("What causes acute coronary syndrome?", "Platelet-mediated thrombosis"))
cards.append(("What are ACS types?", "Unstable angina, NSTEMI, STEMI"))
cards.append(("What is unstable angina?", "Chest pain at rest, unpredictable, may respond to NTG, troponin negative, ST depression or T-wave inversion"))
cards.append(("What is NSTEMI?", "Troponin positive, ST depression, T-wave inversion, unrelenting chest pain"))
cards.append(("What is STEMI?", "Troponin positive, ST elevation in 2+ contiguous leads, unrelenting chest pain"))
cards.append(("What is variant (Prinzmetal's) angina?", "Unstable angina with transient ST elevation due to coronary artery spasm"))
cards.append(("What causes Prinzmetal's angina?", "Coronary spasm with/without atherosclerotic lesions"))
cards.append(("When does Prinzmetal's angina occur?", "At rest, may be cyclic (same time each day)"))
cards.append(("What precipitates Prinzmetal's angina?", "Nicotine, alcohol, cocaine"))
cards.append(("Is troponin positive in Prinzmetal's angina?", "No"))
cards.append(("What relieves Prinzmetal's angina?", "Nitroglycerin; STs return to normal"))

# MANAGEMENT OF ACUTE CHEST PAIN
cards.append(("What is the stat ECG timeline for chest pain?", "Done and read within 10 minutes"))
cards.append(("What does stat ECG allow?", "Categorization to STEMI vs NSTEMI/unstable angina; risk stratification"))
cards.append(("When should aspirin be given in ACS?", "ASAP; chewed; improves morbidity/mortality"))
cards.append(("What anticoagulant is given in ACS?", "Heparin or enoxaparin"))
cards.append(("What antiplatelet agents are used in ACS?", "Clopidogrel (Plavix), abciximab (Reopro), eptifibatide (Integrilin), tirofiban (Aggrastat)"))
cards.append(("When are beta blockers contraindicated in ACS?", "Cocaine-induced ACS, hypotension, bradycardia, phosphodiesterase inhibitor use (Viagra)"))
cards.append(("What type of beta blocker for ACS?", "Cardioselective (metoprolol); NOT non-cardioselective (propranolol)"))
cards.append(("How is ACS pain treated?", "Nitroglycerin, morphine"))

# ECG LEAD CHANGES AND CORONARY ARTERIES
cards.append(("What artery and wall with changes in II, III, aVF?", "RCA, inferior LV"))
cards.append(("What artery and wall with changes in V1-V4?", "LAD, anterior LV"))
cards.append(("What artery and wall with changes in V5, V6, I, aVL?", "Circumflex, lateral LV"))
cards.append(("What artery and wall with changes in V5, V6?", "Low lateral LV"))
cards.append(("What artery and wall with changes in I, aVL?", "High lateral LV"))
cards.append(("What artery and wall with changes in V1, V2?", "RCA, posterior LV"))
cards.append(("What artery and wall with changes in V3R, V4R?", "RCA, right ventricular infarct"))

# INFERIOR MI
cards.append(("What artery occludes in inferior MI?", "RCA"))
cards.append(("What leads show ST elevation in inferior MI?", "II, III, aVF"))
cards.append(("What are reciprocal changes in inferior MI?", "Lateral wall (I, aVL)"))
cards.append(("What conduction disturbances occur with inferior MI?", "2nd-degree Type I AV block, 3rd-degree AV block, SSS, sinus bradycardia"))
cards.append(("What systolic murmur can develop with inferior MI?", "MVR from papillary muscle rupture"))
cards.append(("Why is posterior papillary muscle at risk?", "Only one blood supply source (RCA)"))
cards.append(("What does tachycardia with inferior MI indicate?", "Higher mortality"))
cards.append(("What is inferior MI also associated with?", "RV infarct, posterior MI"))
cards.append(("How should beta blockers and NTG be used in inferior MI?", "With CAUTION"))

# RIGHT VENTRICULAR INFARCT
cards.append(("What percent of inferior MI have RV infarct?", "~30%"))
cards.append(("What artery supplies the right ventricle?", "RCA"))
cards.append(("What determines RV infarct symptoms?", "Size of infarct"))
cards.append(("What ECG shows RV infarct?", "Right-sided ECG (ST elevation in V4R)"))
cards.append(("What are signs/symptoms of RV infarct?", "JVD at 45°, high CVP, hypotension, clear lungs, bradyarrhythmias"))
cards.append(("What is RV infarct treatment?", "Fluids, positive inotropes"))
cards.append(("What to avoid in RV infarct?", "Preload reducers (nitrates, diuretics)"))
cards.append(("Why caution with beta blockers in RV infarct?", "Often cannot give initially due to hypotension"))

# ANTERIOR MI
cards.append(("What artery occludes in anterior MI?", "LAD"))
cards.append(("What leads show ST elevation in anterior MI?", "V1-V4 (precordial)"))
cards.append(("What are reciprocal changes in anterior MI?", "Inferior wall (II, III, aVF)"))
cards.append(("What AV block may develop with anterior MI?", "2nd-degree Type II or RBBB"))
cards.append(("Why Type II block with anterior MI?", "LAD supplies common bundle of His"))
cards.append(("What does Type II block indicate in anterior MI?", "Ominous sign"))
cards.append(("What systolic murmur can develop with anterior MI?", "Ventricular septal defect"))
cards.append(("Does anterior MI have higher mortality than inferior?", "Yes; heart failure more common"))

# LATERAL MI
cards.append(("What leads show ST elevation in lateral MI?", "V5, V6 (low lateral); I, aVL (high lateral)"))
cards.append(("What artery is involved in lateral MI?", "Left circumflex"))

# TREATMENT OF STEMI
cards.append(("What is reperfusion for STEMI?", "PCI or fibrinolytic therapy"))
cards.append(("What is door-to-balloon time for PCI?", "90 minutes"))
cards.append(("What is door-to-drug time for fibrinolytics?", "30 minutes"))
cards.append(("What are eligibility criteria for fibrinolytics?", "ST elevation in 2+ contiguous leads or new LBBB, onset < 12 hrs, pain ≥ 30 min, unresponsive to SL NTG"))

# FIBRINOLYTIC ABSOLUTE CONTRAINDICATIONS
cards.append(("What are absolute contraindications to fibrinolytics?", "Prior intracranial hemorrhage, structural cerebral lesion, intracranial malignancy, ischemic stroke < 3 months, suspected aortic dissection, active bleeding, significant head/facial trauma < 3 months"))

# EVIDENCE OF REPERFUSION
cards.append(("What indicates successful reperfusion?", "Chest pain relief, ST resolution, marked troponin/CK-MB elevation, reperfusion arrhythmias"))
cards.append(("Why does troponin elevate with reperfusion?", "Myocardial 'stunning' when vessel opens"))
cards.append(("What are reperfusion arrhythmias?", "VT, VF, accelerated idioventricular rhythm (AIVR)"))
cards.append(("Why do reperfusion arrhythmias occur?", "Myocardial 'stunning' when vessel opens"))

# POST-PCI CARE
cards.append(("What to monitor post-PCI for reocclusion?", "Chest pain, ST elevation"))
cards.append(("What is vasovagal reaction during sheath removal?", "Hypotension < 90 systolic with/without bradycardia, no compensatory tachycardia, pallor, nausea, yawning, diaphoresis"))
cards.append(("How to manage vasovagal reaction?", "Fluids, atropine"))
cards.append(("What bleeding site to monitor post-PCI?", "Sheath site, retroperitoneal"))
cards.append(("What are signs of retroperitoneal bleed?", "Sudden hypotension, severe low back pain"))
cards.append(("How long to hold manual pressure post-sheath removal?", "Minimum 20 min (30 min if on GP IIb/IIIa inhibitors)"))

# TREATMENT OF NSTEMI
cards.append(("Is emergent reperfusion needed for NSTEMI?", "No"))
cards.append(("What meds for NSTEMI?", "Same as STEMI"))
cards.append(("When is cardiac cath done for NSTEMI?", "Within 24 hours if high risk or continued chest pain/instability"))
cards.append(("What to start if high-risk NSTEMI?", "GP IIb/IIIa inhibitors (Integrilin, Reopro)"))

# COMPLICATIONS OF ACUTE MI
cards.append(("What is the most common complication of acute MI?", "Arrhythmias"))
cards.append(("What are life-threatening arrhythmias post-MI?", "VT, VF"))
cards.append(("How to treat VF?", "Defibrillate"))
cards.append(("How to treat stable sustained VT?", "Drug therapy"))
cards.append(("How to treat unstable sustained VT?", "Synchronized cardioversion"))
cards.append(("What other complications of acute MI?", "Bradycardia, heart blocks, SSS, atrial fibrillation, heart failure, cardiogenic shock, reinfarction, thromboembolism, pericarditis, ventricular aneurysm, VSD, papillary muscle rupture, wall rupture"))
cards.append(("How does atrial fibrillation affect MI mortality?", "Increases risk 10-15%, even if returned to NSR"))

# INTERVENTIONAL CARDIOLOGY
cards.append(("What is goal of PCI with stent?", "Restoration of blood flow distal to coronary lesion"))
cards.append(("What is most common PCI procedure?", "Intracoronary stenting"))
cards.append(("What is in-hospital death rate for PCI?", "~1.8%"))
cards.append(("What is in-hospital MI rate for PCI?", "~0.4%"))
cards.append(("What are PCI complications?", "Coronary perforation, distal embolization, intramural hematoma, stent deployment failure, stent thrombosis, stroke/TIA, arrhythmias, renal failure, retroperitoneal bleed"))
cards.append(("When does stent thrombosis most likely occur?", "Acutely (< 24 hours) or subacutely (< 30 days)"))

# HYPERTENSIVE CRISIS
cards.append(("What is hypertensive emergency/crisis?", "Elevated BP with end organ damage (brain, heart, kidney, retina)"))
cards.append(("What is hypertensive urgency?", "Elevated BP without acute end organ damage"))
cards.append(("What is greatest risk of hypertensive crisis?", "Stroke"))
cards.append(("What is treatment of hypertensive crisis?", "Emergent BP lowering; nitroprusside or labetalol"))
cards.append(("What is nitroprusside?", "Preload and afterload reducer"))
cards.append(("What is cyanide toxicity from nitroprusside?", "Mental status change, tachycardia, seizure, need for increased dose, unexplained metabolic acidosis"))
cards.append(("When is cyanide toxicity more likely?", "Renal impairment or drug use > 24 hours"))
cards.append(("What is labetalol dosing preference?", "Intermittent IV doses (max 300 mg total)"))
cards.append(("How long does labetalol effect persist?", "4-6 hours after IV dose"))

# PERIPHERAL ARTERIAL DISEASE
cards.append(("What are the 6 Ps of PAD?", "Pain, pallor, pulse absent/diminished, paresthesia, paralysis, poikilothermia"))
cards.append(("What is poikilothermia?", "Loss of hair on toes/legs, glossy/thin/cool/dry skin"))
cards.append(("What is ankle-brachial index (ABI)?", "Test to assess lower extremity perfusion"))
cards.append(("What is normal ABI?", "> 0.90"))
cards.append(("How is ABI calculated?", "Ankle pressure ÷ brachial pressure (same side)"))
cards.append(("What are PAD treatments?", "Embolectomy, bypass graft, angioplasty"))
cards.append(("What bed position for PAD?", "Reverse Trendelenburg"))
cards.append(("Should you elevate affected extremity in PAD?", "NO - decreases perfusion"))
cards.append(("What medications for PAD?", "Thrombolytics (tPA), anticoagulants (heparin), antiplatelet agents (ASA, clopidogrel), vasodilators"))

# CAROTID ARTERY DISEASE
cards.append(("What are signs/symptoms of acute carotid artery disease?", "TIA, monocular visual disturbances, aphasia, stroke"))
cards.append(("What is gold standard diagnostic test for carotid disease?", "Angiography (risk of stroke during exam)"))
cards.append(("What are carotid artery disease treatments?", "Carotid endarterectomy (CEA), carotid stenting, aspirin, statin therapy"))
cards.append(("What to monitor post-carotid procedure?", "Frequent neurological/motor checks, BP/HR (labile BP/bradyarrhythmia possible), bleeding"))
cards.append(("What is hypoperfusion syndrome post-carotid procedure?", "Headache ipsilateral to revascularized artery, focal motor seizures, intracerebral hemorrhage"))

# WPW
cards.append(("What is Wolff-Parkinson-White syndrome?", "Genetic conduction abnormality with abnormal pathway bypassing AV node"))
cards.append(("What age group has WPW?", "< 30 years old"))
cards.append(("What does ECG show in WPW sinus rhythm?", "Short PR interval, delta wave"))
cards.append(("What arrhythmia does WPW cause?", "SVT; may also have pre-excited atrial fibrillation"))
cards.append(("What is pre-excited atrial fibrillation?", "Irregular rhythm, rate ≥ 150 bpm, wide QRS"))
cards.append(("What are WPW symptoms during SVT?", "Palpitations, dizziness, chest pain, SOB, syncope"))
cards.append(("What is definitive WPW treatment?", "Radiofrequency ablation"))
cards.append(("How to treat unstable SVT in WPW?", "Synchronized cardioversion or adenosine"))
cards.append(("How to treat pre-excited AF in WPW?", "Beta blockers, amiodarone, or procainamide IV"))
cards.append(("What NOT to give for pre-excited AF in WPW?", "Adenosine, digoxin, calcium channel blockers"))
cards.append(("Why avoid adenosine/digoxin/CCB in pre-excited AF?", "May enhance antegrade conduction through abnormal pathway by increasing AV node refractory period → VF"))

# QT PROLONGATION
cards.append(("What causes QT prolongation?", "Drugs (amiodarone, quinidine, haloperidol, procainamide), electrolyte problems (hypokalemia, hypocalcemia, hypomagnesemia)"))
cards.append(("What can QT prolongation lead to?", "Torsades de pointes"))
cards.append(("What is treatment for torsades VT?", "Magnesium"))

# PACEMAKER CODE
cards.append(("What does first letter of pacemaker code indicate?", "Chamber paced"))
cards.append(("What does second letter of pacemaker code indicate?", "Chamber sensed"))
cards.append(("What does third letter of pacemaker code indicate?", "Response to sensing"))
cards.append(("What does I mean in pacemaker code?", "Inhibits (demand pacing)"))
cards.append(("What does D mean in pacemaker code?", "Inhibits and triggers (dual)"))
cards.append(("What does O mean in pacemaker code?", "None"))
cards.append(("What is DDD pacemaker?", "Paces both chambers, senses both, can inhibit and trigger"))
cards.append(("What is VVI pacemaker?", "Paces ventricle, senses ventricle, inhibits in response to sensing"))

# PACEMAKER MALFUNCTIONS
cards.append(("What are 3 basic pacer malfunctions?", "Failure to pace, failure to capture, failure to sense"))
cards.append(("What is failure to pace?", "No spike when expected"))
cards.append(("What is failure to capture?", "Spikes without QRS (for ventricular pacing)"))
cards.append(("What is failure to sense?", "Pacing in native beats"))

# ICD
cards.append(("What tiered therapy can ICDs provide?", "Programmed to shock, burst pace, provide pacing for bradyarrhythmias"))
cards.append(("What is ICD burst pacing?", "Sense tachyarrhythmia, provide beats faster than tachyarrhythmia, suddenly stop (hope for SA node recovery)"))
cards.append(("If ICD does not correct arrhythmia, what to do?", "Shock as usual; do not place pads directly over ICD"))
cards.append(("What patient education needed for ICD?", "Device function, emotional support (fear of being shocked)"))

# HEART FAILURE BASICS
cards.append(("What is heart failure?", "Clinical syndrome with signs/symptoms of high intracardiac pressures and decreased CO"))
cards.append(("What is acute decompensated heart failure?", "Abrupt onset of severe symptoms requiring hospitalization"))
cards.append(("What percent of acute decompensated HF have chronic HF history?", "~75%"))
cards.append(("What is heart failure with systolic dysfunction?", "EF ≤ 40%, problem with ejection"))
cards.append(("What is heart failure with diastolic dysfunction?", "EF > 50%, problem with filling"))

# BNP
cards.append(("What is BNP?", "B-type natriuretic peptide"))
cards.append(("Why is BNP released?", "Ventricle under wall stress; attempts to dilate and decrease ventricular pressure"))
cards.append(("When does BNP elevate?", "LV failure (or to lesser degree, RV stress from pulmonary HTN/PE)"))

# SYSTOLIC VS DIASTOLIC HF
cards.append(("What is pathophysiology of systolic dysfunction?", "Decreased contractility → decreased CO → compensatory mechanisms (SNS, RAAS) → fluid retention"))
cards.append(("What causes systolic HF remodeling over time?", "Prolonged compensatory hormone effects"))
cards.append(("What drugs decrease neurohormonal effects in HF?", "ACE inhibitors, ARBs, beta blockers, aldosterone antagonists"))
cards.append(("What is heart size on CXR in systolic HF?", "May be large/dilated or normal"))
cards.append(("What is PMI shift in systolic HF?", "From midclavicular to left (if enlarged heart)"))
cards.append(("What is heart size on CXR in diastolic HF?", "Generally normal"))
cards.append(("What may ECG show in diastolic HF?", "LV hypertrophy pattern (especially with uncontrolled HTN)"))

# RIGHT VS LEFT SIDED HF
cards.append(("What causes right-sided HF?", "Pulmonary HTN, cor pulmonale, RV infarct, left-sided HF, tricuspid/pulmonic valve disease"))
cards.append(("What causes left-sided HF?", "CAD, MI, HTN, cardiomyopathy, mitral/aortic valve disease"))
cards.append(("What are signs/symptoms of right-sided HF?", "JVD, peripheral edema, hepatomegaly, ascites, weight gain"))
cards.append(("What are signs/symptoms of left-sided HF?", "Dyspnea, orthopnea, PND, pulmonary crackles, S3, cough, fatigue"))

# HF CLASSIFICATIONS
cards.append(("What is AHA Stage A heart failure?", "High risk; no dysfunction"))
cards.append(("What is AHA Stage B heart failure?", "Heart disorder/structural defect; no symptoms"))
cards.append(("What is AHA Stage C heart failure?", "Heart disorder/structural defect with symptoms (past or present)"))
cards.append(("What is AHA Stage D heart failure?", "End-stage with symptoms despite maximal therapy"))
cards.append(("What is NYHA Class I heart failure?", "Ordinary activity does not cause symptoms; extraordinary activity does"))
cards.append(("What is NYHA Class II heart failure?", "Comfortable at rest; ordinary activity causes symptoms"))
cards.append(("What is NYHA Class III heart failure?", "Comfortable at rest; minimal activity causes symptoms"))
cards.append(("What is NYHA Class IV heart failure?", "Symptoms at rest; severe limitation of physical activity"))
cards.append(("What is main cause of death from HF?", "Sudden death arrhythmia"))
cards.append(("What NYHA classes may need ICD?", "Class II to IV"))

# CARDIOMYOPATHY
cards.append(("What is dilated cardiomyopathy?", "Enlarged heart, decreased contractility, systolic dysfunction"))
cards.append(("What causes dilated cardiomyopathy?", "Idiopathic, viral, alcohol, chemotherapy, peripartum"))
cards.append(("What is EF in dilated cardiomyopathy?", "< 40%"))
cards.append(("What is hypertrophic cardiomyopathy?", "Thickened ventricular wall, decreased compliance, diastolic dysfunction"))
cards.append(("What causes hypertrophic cardiomyopathy?", "Genetic (autosomal dominant)"))
cards.append(("What is EF in hypertrophic cardiomyopathy?", "Normal or increased (> 50%)"))
cards.append(("What heart sound in hypertrophic cardiomyopathy?", "S4"))
cards.append(("What drugs for dilated cardiomyopathy?", "Increase contractility, decrease preload and afterload"))
cards.append(("What drugs for hypertrophic cardiomyopathy?", "Beta blockers, calcium channel blockers (decrease HR, increase filling time)"))

# CARDIOGENIC SHOCK
cards.append(("What is cardiogenic shock?", "Most extreme HF when compensatory mechanisms fail"))
cards.append(("What causes cardiogenic shock?", "Extreme drop in SV from systolic dysfunction"))
cards.append(("What is result of cardiogenic shock?", "Elevated PAOP, elevated SVR, decreased CO, inadequate organ perfusion"))
cards.append(("What are etiologies of cardiogenic shock?", "Acute MI, chronic HF, cardiomyopathy, dysrhythmias, tamponade, papillary muscle rupture"))
cards.append(("Why is papillary muscle rupture life-threatening?", "Obliterates mitral valve; requires immediate surgery"))
cards.append(("What are signs of cardiogenic shock?", "Hypotension, tachycardia, decreased urine output, cool/clammy skin, altered mental status, elevated PAOP, low CO/CI"))
cards.append(("What is treatment of cardiogenic shock?", "Identify cause, manage arrhythmias, reperfusion if STEMI, emergent surgery if mechanical problem, mechanical support"))

# IABP
cards.append(("What is IABP used for?", "LV heart failure, cardiogenic shock, cardiomyopathies, bridge to transplant"))
cards.append(("What does balloon do?", "Inflates and deflates"))
cards.append(("When does balloon inflate?", "At dicrotic notch, beginning of diastole"))
cards.append(("What are benefits of balloon inflation?", "Increases coronary artery perfusion, increases diastolic BP"))
cards.append(("When does balloon deflate?", "Right before systole"))
cards.append(("What triggers balloon deflation?", "R-wave of ECG or upstroke of arterial pressure wave"))
cards.append(("What are benefits of balloon deflation?", "Decreases afterload, decreases myocardial oxygen demand, increases CO/SV"))

# CARDIAC SURGERY - CABG
cards.append(("What happens during cardiopulmonary bypass?", "Aortic cross-clamping, heart stopped"))
cards.append(("What are common cannulation sites for bypass?", "Aorta, right atrium"))
cards.append(("What does longer bypass time cause?", "More bleeding, more complications"))
cards.append(("What is priming during bypass?", "Hemodilution with isotonic crystalloids; enhances oxygenation"))
cards.append(("What temperature during bypass?", "Hypothermia (28-36°C)"))
cards.append(("What anticoagulation during bypass?", "Large heparin doses"))
cards.append(("How is cardiac arrest achieved during bypass?", "Potassium cardioplegic agent infused during diastole"))

# POST-CABG COMPLICATIONS
cards.append(("What are post-CABG complications?", "Hemodynamic abnormalities, arrhythmias, tamponade, pericarditis, electrolyte abnormalities, bleeding, pulmonary problems, pain/anxiety, renal failure, glycemic control issues, GI problems, infections"))

# CHEST TUBE MANAGEMENT POST-CABG
cards.append(("How to maintain chest tube patency?", "No dependent loops; gently milk if clots appear"))
cards.append(("Is routine milking/stripping of chest tubes indicated?", "No"))
cards.append(("What do mediastinal chest tubes remove?", "Serosanguinous fluid from operative site"))
cards.append(("What do pleural chest tubes remove?", "Air, blood, serous fluid from pleural space"))
cards.append(("Where to keep chest tubes?", "Lower than patient's chest"))
cards.append(("When to clamp chest tubes?", "Only when changing drainage system or system disconnect"))
cards.append(("Why not clamp chest tubes routinely?", "Loses connection to negative chamber"))
cards.append(("What chest tube output requires intervention?", "> 100 mL for 2 consecutive hours"))
cards.append(("How to maintain hemodynamic stability post-CABG?", "Correct volume status, administer blood products"))

# VALVE SURGERY
cards.append(("What are mechanical valve advantages?", "Durable, long-lasting"))
cards.append(("What are mechanical valve disadvantages?", "Require lifelong anticoagulation"))
cards.append(("What are biological valve advantages?", "No lifelong anticoagulation (only antiplatelet)"))
cards.append(("What are biological valve disadvantages?", "Less durable, may need replacement"))
cards.append(("What anticoagulation for mechanical valve?", "Warfarin (lifelong)"))
cards.append(("What anticoagulation for biological valve?", "Antiplatelet therapy (aspirin)"))

# POST-VALVE SURGERY CARE
cards.append(("Why avoid drop in preload post-valve surgery?", "Patients had elevated end-diastolic volumes; sudden normalization causes hypotension"))
cards.append(("Why anticipate conduction disturbances post-valve surgery?", "Valves anatomically close to conduction pathways"))
cards.append(("What may be needed post-valve surgery for conduction?", "Temporary or permanent pacing"))

# TAVR
cards.append(("What is TAVR?", "Transcatheter aortic valve replacement"))
cards.append(("When was TAVR approved?", "2011"))
cards.append(("What is TAVR procedure?", "Placement of collapsible prosthetic valve (bovine/porcine) over diseased valve"))
cards.append(("What is TAVR access?", "Percutaneous or small incision; usually femoral artery"))
cards.append(("Where is TAVR performed?", "Modified cardiac cath lab"))
cards.append(("Who are ideal TAVR candidates?", "Severe aortic valve disease, high-risk for open surgery"))
cards.append(("Can intermediate-risk patients get TAVR?", "Yes, if heart valve team decides"))
cards.append(("Are extreme high-risk/inoperable or low-risk patients TAVR candidates?", "No"))
cards.append(("What are TAVR complications?", "Vascular complications (hematomas, retroperitoneal bleed, arterial occlusion), heart block, stroke, AKI, paravalvular regurgitation"))
cards.append(("What antiplatelet therapy post-TAVR?", "Aspirin 75-100 mg/day for life; clopidogrel 75 mg/day for 3-6 months"))

# CARDIAC TAMPONADE
cards.append(("What are tamponade etiologies?", "Post-cardiac surgery, pericarditis, pericardial effusion, trauma"))
cards.append(("What are signs/symptoms of tamponade?", "Restlessness, agitation, hypotension, elevated JVD, equalization of pressures (CVP=PAD=PAOP), muffled heart sounds, enlarged cardiac silhouette, narrowed pulse pressure, pulsus paradoxus"))
cards.append(("What is example of narrowed pulse pressure in tamponade?", "82/68"))
cards.append(("What is pulsus paradoxus?", "Excessive drop (> 12 mmHg) in SBP during inspiration"))
cards.append(("What causes pulsus paradoxus in tamponade?", "Cardiac restriction with inspiration; increased intrathoracic pressure, decreased venous return"))
cards.append(("How is pulsus paradoxus best seen?", "Respiratory variation on arterial waveform"))
cards.append(("What is treatment for post-op cardiac surgery tamponade?", "Emergent return to OR"))
cards.append(("What is treatment for medical tamponade?", "Emergent pericardiocentesis"))

# CARDIAC TRAUMA
cards.append(("Which valve most at risk for trauma rupture?", "Aortic valve (most anterior)"))
cards.append(("What differentiates myocardial contusion from pericarditis?", "Pericarditis has friction rub, pain worse with inspiration/positional; contusion has MI-like symptoms"))

# ANEURYSMS
cards.append(("What is an aneurysm?", "Localized blood-filled outpouching in artery wall"))
cards.append(("What determines rupture risk?", "Size (larger = more likely to rupture)"))
cards.append(("What are aneurysm etiologies?", "Arteriosclerosis, HTN, smoking, obesity, bacterial infection, congenital, trauma, Marfan syndrome"))
cards.append(("What percent of CV aneurysms are abdominal aortic?", "75%"))
cards.append(("What are AAA signs/symptoms?", "Asymptomatic if small, abdominal pulsations, abdominal/low back pain, nausea, vomiting, shock"))
cards.append(("What percent of CV aneurysms are thoracic aortic?", "25%"))
cards.append(("What are thoracic aneurysm signs/symptoms?", "Sudden tearing/ripping chest pain radiating to shoulders/neck/back, cough, hoarseness, dysphagia, dyspnea, dizziness, difficulty walking/speaking, widened mediastinum on CXR"))

# ANEURYSM TREATMENT
cards.append(("How to treat aneurysm < 5 cm with no symptoms?", "Monitor regularly (ultrasound/CT), treat HTN with beta blockers"))
cards.append(("Are Marfan patients treated sooner for aneurysm?", "Yes"))
cards.append(("How to treat thoracic aneurysm > 6 cm or symptomatic?", "Surgical repair"))
cards.append(("What is treatment for dissection?", "SURGERY; aggressive HTN and HR control (labetalol drip)"))

# AORTIC DISSECTION
cards.append(("What is aortic dissection?", "Blood passes through inner lining between aortic layers"))
cards.append(("What is tear pattern in dissection?", "Spiral"))
cards.append(("Can dissection occur suddenly or gradually?", "Both"))
cards.append(("Where does dissection occur?", "Ascending aorta or aortic arch"))
cards.append(("Is dissection life-threatening?", "Yes; requires immediate surgical intervention"))

# Add medication cards
cards.append(("What is aspirin used for in ACS?", "Antiplatelet; reduces mortality"))
cards.append(("What is clopidogrel (Plavix)?", "Antiplatelet; ADP receptor antagonist; prevents platelet aggregation"))
cards.append(("What is abciximab (Reopro)?", "GP IIb/IIIa inhibitor; antiplatelet; prevents platelet aggregation"))
cards.append(("What is eptifibatide (Integrilin)?", "GP IIb/IIIa inhibitor; antiplatelet; prevents platelet aggregation"))
cards.append(("What is tirofiban (Aggrastat)?", "GP IIb/IIIa inhibitor; antiplatelet; prevents platelet aggregation"))
cards.append(("What is metoprolol (Lopressor)?", "Cardioselective beta blocker; decreases HR, contractility, BP; for ACS, HTN, HF"))
cards.append(("What is propranolol (Inderal)?", "Non-cardioselective beta blocker; affects heart and lungs; avoid in ACS"))
cards.append(("What is nitroglycerin?", "Nitrate; vasodilator; decreases preload; for angina, ACS, HF"))
cards.append(("What is morphine used for in ACS?", "Pain relief; decreases anxiety, preload, afterload"))
cards.append(("What is heparin?", "Anticoagulant; prevents clot formation/extension; for ACS"))
cards.append(("What is enoxaparin?", "Low molecular weight heparin; anticoagulant; for ACS"))
cards.append(("What is nitroprusside (Nipride)?", "Preload and afterload reducer; for hypertensive crisis"))
cards.append(("What is labetalol (Normodyne)?", "Alpha and beta blocker; for hypertensive crisis; duration 4-6 hours"))
cards.append(("What is furosemide (Lasix)?", "Loop diuretic; decreases preload; for HF, pulmonary edema"))
cards.append(("What is digoxin?", "Cardiac glycoside; weak positive inotrope; slows AV conduction; for HF, atrial fibrillation"))
cards.append(("What is dopamine at low dose (< 5 mcg/kg/min)?", "Dopaminergic; renal vasodilation"))
cards.append(("What is dopamine at medium dose (5-10 mcg/kg/min)?", "Beta-1 agonist; positive inotrope"))
cards.append(("What is dopamine at high dose (> 10 mcg/kg/min)?", "Alpha agonist; vasoconstriction"))
cards.append(("What is dobutamine?", "Beta-1 agonist; positive inotrope; for HF, cardiogenic shock"))
cards.append(("What is milrinone?", "Phosphodiesterase inhibitor; positive inotrope and vasodilator; for HF"))
cards.append(("What is atropine?", "Anticholinergic; increases HR; for symptomatic bradycardia"))
cards.append(("What is amiodarone?", "Antiarrhythmic; for VT, VF, atrial fibrillation; causes QT prolongation"))
cards.append(("What is adenosine?", "Antiarrhythmic; slows AV conduction; for SVT; avoid in pre-excited AF"))
cards.append(("What is magnesium used for in arrhythmias?", "Treatment for torsades de pointes"))
cards.append(("What is alteplase (tPA)?", "Fibrinolytic; breaks down clots; for STEMI, ischemic stroke, PE"))

# Save all cards to TSV
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
with open("ccrn_cardio_cards.tsv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(["Question", "Answer", "Tags"])
    for question, answer in unique_cards:
        # Determine tags based on content
        tags = ["ccrn::cardio"]

        # Add specific tags
        if any(word in question.lower() for word in ['s1', 's2', 's3', 's4', 'sound', 'murmur', 'auscult']):
            tags.append("heart_sounds")
        if any(word in question.lower() for word in ['valve', 'stenosis', 'insufficiency', 'regurgitation', 'mitral', 'aortic', 'tricuspid', 'pulmonic']):
            tags.append("valves")
        if any(word in question.lower() for word in ['bp', 'blood pressure', 'pulse pressure', 'systolic', 'diastolic']):
            tags.append("hemodynamics")
        if any(word in question.lower() for word in ['acs', 'mi', 'stemi', 'nstemi', 'angina', 'infarct', 'coronary']):
            tags.append("acs")
        if any(word in question.lower() for word in ['lead', 'ecg', 'rca', 'lad', 'circumflex', 'ii', 'iii', 'avf', 'v1', 'v2', 'v3', 'v4']):
            tags.append("ecg")
        if any(word in question.lower() for word in ['inferior', 'anterior', 'lateral', 'posterior', 'rv infarct', 'right ventricular']):
            tags.append("mi_types")
        if any(word in question.lower() for word in ['pci', 'fibrinolytic', 'reperfusion', 'stent', 'balloon']):
            tags.append("interventions")
        if any(word in question.lower() for word in ['hypertensive', 'crisis', 'emergency', 'urgency']):
            tags.append("hypertension")
        if any(word in question.lower() for word in ['pad', 'peripheral', 'arterial', 'abi', 'carotid']):
            tags.append("vascular")
        if any(word in question.lower() for word in ['wpw', 'qt', 'arrhythmia', 'vt', 'vf', 'torsades', 'block']):
            tags.append("dysrhythmias")
        if any(word in question.lower() for word in ['pacemaker', 'pacer', 'vvi', 'ddd', 'icd']):
            tags.append("devices")
        if any(word in question.lower() for word in ['heart failure', 'hf', 'systolic', 'diastolic', 'bnp', 'nyha', 'aha']):
            tags.append("hf")
        if any(word in question.lower() for word in ['cardiomyopathy', 'dilated', 'hypertrophic']):
            tags.append("cardiomyopathy")
        if any(word in question.lower() for word in ['cardiogenic shock', 'shock']):
            tags.append("shock")
        if any(word in question.lower() for word in ['iabp', 'balloon pump', 'inflate', 'deflate']):
            tags.append("iabp")
        if any(word in question.lower() for word in ['cabg', 'bypass', 'valve surgery', 'tavr', 'cardiac surgery']):
            tags.append("cardiac_surgery")
        if any(word in question.lower() for word in ['tamponade', 'pulsus paradoxus']):
            tags.append("tamponade")
        if any(word in question.lower() for word in ['aneurysm', 'dissection', 'aaa', 'thoracic']):
            tags.append("aneurysm")
        if any(word in (question + " " + answer).lower() for word in ['aspirin', 'clopidogrel', 'plavix', 'metoprolol', 'lopressor', 'nitroglycerin', 'morphine', 'heparin', 'enoxaparin', 'nitroprusside', 'labetalol', 'furosemide', 'lasix', 'digoxin', 'dopamine', 'dobutamine', 'milrinone', 'atropine', 'amiodarone', 'adenosine', 'magnesium', 'alteplase', 'tpa']):
            tags.append("meds")

        tags_str = " ".join(tags)
        writer.writerow([f"Question:\n{question}", f"Answer:\n{answer}", tags_str])

print(f"Saved {len(unique_cards)} cards to ccrn_cardio_cards.tsv")
