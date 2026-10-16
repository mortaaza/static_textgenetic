# Content for the generated pages. Edit here, then run: python3 scripts/build_pages.py
# Keep company facts consistent with index.html — only claims already made on the site.

SITE = "https://www.textgenetic.com"

TOPICS = [
    {
        "slug": "neuroanalytics",
        "crumb": "Neuroanalytics",
        "kicker": "Brain health",
        "title": "Neuroanalytics & digital biomarkers for neurodegenerative disease — TextGenetic AI",
        "description": "How TextGenetic AI turns gait, balance, cognition, speech and medication-response signals into neural biomarkers and progression analytics for Parkinson's, Alzheimer's and cognitive decline.",
        "h1": "Neuroanalytics: turning clinical signals into <em class=\"acc\">neural biomarkers</em>",
        "lead": "Neurodegenerative conditions change slowly and unevenly. A single clinic visit captures a snapshot; what clinicians and researchers need is the trend. Our neuroanalytics platform captures the signals that matter, over time, and makes them measurable.",
        "body": """
<h2>What we capture</h2>
<p>Specialized care already generates rich signals — they are just scattered across assessments, notes and devices. We structure them into longitudinal records:</p>
<ul>
  <li><strong>Gait and balance</strong> — walking speed, stride variability, turning, and episodes of <a href="/glossary/freezing-of-gait/">freezing of gait</a>.</li>
  <li><strong>Cognition</strong> — standardized assessment scores and their change over time.</li>
  <li><strong>Speech</strong> — rhythm, pacing and articulation features that shift with disease progression.</li>
  <li><strong>Medication response</strong> — how symptoms track against dosing, so "on/off" patterns become visible.</li>
</ul>

<h2>From signals to biomarkers</h2>
<p>A <a href="/glossary/digital-biomarker/">digital biomarker</a> is a measurable feature, derived from data, that reflects a biological or clinical state. We do not start from the model; we start from the capture. Clean, consistent, de-identified <a href="/glossary/longitudinal-data/">longitudinal data</a> is the raw material, and pattern mining on that data is what surfaces candidate biomarkers worth validating.</p>
<p>Across Parkinson's disease, Alzheimer's disease and mild cognitive impairment, the questions are similar: who is progressing faster, which signals change first, and which patients share a trajectory. Identifying clinically meaningful <a href="/glossary/parkinsons-disease-subtypes/">subtypes</a> is one of the most useful outcomes of this work.</p>

<h2>Built for clinicians, ready for research</h2>
<ul>
  <li><strong><a href="/glossary/clinician-in-the-loop/">Clinician in the loop</a>.</strong> The platform assists with assessment and documentation; a qualified person always makes the clinical call. Nothing is autonomous.</li>
  <li><strong><a href="/glossary/de-identification/">De-identified by design</a>.</strong> Research-ready data foundations with governance built in, not bolted on.</li>
  <li><strong>Reproducible pipelines.</strong> Analyses are containerized and versioned, so results can be re-run and audited.</li>
</ul>

<h2>Where this comes from</h2>
<p>Our forecasting engine was first validated in a very different setting — predictive maintenance for a municipal fleet in the <a href="/predictive-maintenance-ai/">City of Kitchener pilot</a> — and was selected for Canada's <a href="/isc-testing-stream/">ISC Testing Stream</a>. The same discipline of measured, reviewable prediction now underpins our brain-health work with a multi-site neurodegenerative-care provider.</p>
""",
        "related": ["digital-biomarker", "neuroanalytics", "freezing-of-gait", "parkinsons-disease-subtypes", "longitudinal-data"],
    },
    {
        "slug": "health-workflow-automation",
        "crumb": "Workflow automation",
        "kicker": "Specialized care",
        "title": "Health workflow automation for specialized care — TextGenetic AI",
        "description": "Care coordination, reassessment tracking and clinician-reviewed documentation support for multi-site neurodegenerative-care programs. One coordinated, privacy-conscious view.",
        "h1": "Workflow automation for <em class=\"acc\">specialized care</em>",
        "lead": "Specialized clinics run on lists, paper and memory: who is due for reassessment, which program a patient is in, who owns the follow-up. Our platform replaces that with one coordinated view — so staff spend their time on patients, not on tracking.",
        "body": """
<h2>The problem we see in every clinic</h2>
<p>Patient, program and assessment data lives in different systems and spreadsheets. Reassessment windows are missed, follow-ups fall through the gaps between sites, and documentation is written late at night. None of this is a people problem; it is a workflow problem.</p>

<h2>What the platform does</h2>
<ul>
  <li><strong>Central care registry.</strong> Every patient, program and milestone in one place, across sites.</li>
  <li><strong><a href="/glossary/reassessment-tracking/">Reassessment tracking</a>.</strong> Due dates computed automatically from program rules; nothing waits on a spreadsheet.</li>
  <li><strong>Follow-up ownership.</strong> Each open item has a named owner and a visible status.</li>
  <li><strong>Documentation support.</strong> AI-assisted drafting with <a href="/glossary/clinician-in-the-loop/">clinician review</a> — faster notes, same accountability.</li>
</ul>

<h2>Automation that respects clinical judgment</h2>
<p>We draw a hard line: the system organizes, reminds, drafts and surfaces patterns. It never makes an autonomous clinical decision. That principle shapes every feature, from how suggestions are presented to how overrides are logged.</p>

<h2>A foundation for analytics</h2>
<p>Once care data is structured and consistent, it becomes the basis for something larger: longitudinal <a href="/neuroanalytics/">neuroanalytics</a> and candidate <a href="/glossary/digital-biomarker/">digital biomarkers</a>. The workflow layer and the analytics layer are two halves of the same platform — which is how we built it for a multi-site neurodegenerative-care provider.</p>
""",
        "related": ["care-coordination", "reassessment-tracking", "clinician-in-the-loop", "de-identification"],
    },
    {
        "slug": "predictive-maintenance-ai",
        "crumb": "Case study: City of Kitchener",
        "kicker": "Case study · Municipal · 2025",
        "title": "AI predictive maintenance for municipal fleets — City of Kitchener pilot | TextGenetic AI",
        "description": "How TextGenetic AI won a $100,000 Pitch Kitchener pilot to apply real-time predictive analytics to the City of Kitchener's fleet, and productized it as Axion Fleet.",
        "h1": "Predictive maintenance for a city fleet: the <em class=\"acc\">Kitchener pilot</em>",
        "lead": "Chosen as one of three companies from ten finalists at Communitech's Fast Track Cities showcase, TextGenetic AI won a $100,000 Pitch Kitchener pilot to apply AI-driven, real-time predictive analytics to the City of Kitchener's vehicle fleet.",
        "body": """
<h2>The challenge</h2>
<p>A municipal fleet is hundreds of vehicles and assets with different ages, duty cycles and maintenance histories. Breakdowns are expensive twice over: the repair itself, and the service that doesn't get delivered while a vehicle is off the road. Maintenance schedules based on fixed intervals either over-service healthy vehicles or miss the ones about to fail.</p>

<h2>What we built</h2>
<p>Our platform ingests historical work orders and telematics data and forecasts the likelihood of component failures, so crews act before a breakdown rather than after. It is <a href="/glossary/predictive-maintenance/">predictive maintenance</a> in the practical sense: a prioritized list of what to look at this week.</p>
<ul>
  <li>Flags potential maintenance issues before they become costly breakdowns</li>
  <li>Reduces vehicle downtime and extends the life of city assets</li>
  <li>Lowers operating costs and supports environmental goals</li>
</ul>

<h2>Why it matters beyond fleets</h2>
<p>The pilot is where our forecasting engine earned its credibility in live operations. The Government of Canada then selected the technology for its <a href="/isc-testing-stream/">Innovative Solutions Canada Testing Stream</a>, a program that tests late-stage innovations (<a href="/glossary/technology-readiness-level/">TRL 7–9</a>) in real federal environments. The same engine — and the same discipline of measured, reviewable prediction — now powers our <a href="/neuroanalytics/">neuroanalytics</a> work in brain health.</p>

<h2>Productized as Axion Fleet</h2>
<p>The pilot has been productized as <a href="https://axionfleetai.com" target="_blank" rel="noopener">Axion Fleet</a>: asset lifecycle, automated work orders and predictive maintenance for municipal and commercial fleets.</p>

<h2>Coverage</h2>
<ul>
  <li><a href="https://www.kitchener.ca/news/posts/modernizing-municipal-fleet-management-with-ai/" target="_blank" rel="noopener">City of Kitchener — Modernizing municipal fleet management with AI</a></li>
  <li><a href="https://communitech.ca/technews/three-waterloo-region-tech-companies-selected-to-pilot-solutions-with-city-of-kitchener.html" target="_blank" rel="noopener">Communitech — Three Waterloo Region tech companies selected to pilot solutions with City of Kitchener</a></li>
</ul>
""",
        "related": ["predictive-maintenance", "technology-readiness-level", "innovative-solutions-canada-testing-stream"],
    },
    {
        "slug": "isc-testing-stream",
        "crumb": "ISC Testing Stream",
        "kicker": "Credentials",
        "title": "Selected for Canada's Innovative Solutions Canada Testing Stream — TextGenetic AI",
        "description": "TextGenetic AI has been selected for the Government of Canada's Innovative Solutions Canada (ISC) Testing Stream, which procures and tests late-stage Canadian innovations in real operations.",
        "h1": "Selected for the <em class=\"acc\">ISC Testing Stream</em>",
        "lead": "Innovative Solutions Canada (ISC) is a Government of Canada program that buys and tests pre-commercial Canadian innovations in real operational environments. TextGenetic AI has been selected for its Testing Stream.",
        "body": """
<h2>What the Testing Stream is</h2>
<p>The <a href="/glossary/innovative-solutions-canada-testing-stream/">ISC Testing Stream</a> evaluates late-stage innovations — <a href="/glossary/technology-readiness-level/">Technology Readiness Levels 7 to 9</a> — through federal R&amp;D contracts. A federal department tests the innovation in its own operations and reports on how it performed. Successful testing opens a direct pathway to commercialization with the federal government.</p>

<h2>Why it matters</h2>
<ul>
  <li><strong>Independent validation.</strong> The evidence that our AI performs comes from a federal evaluator, not from us.</li>
  <li><strong>Real operations, not a lab.</strong> Testing happens in live settings with real data and real users.</li>
  <li><strong>Late-stage maturity.</strong> Selection confirms the technology is deployable, not a prototype.</li>
</ul>

<h2>Where the technology was proven first</h2>
<p>Our predictive-AI platform earned its field record in the <a href="/predictive-maintenance-ai/">City of Kitchener fleet pilot</a>. That track record, and the discipline behind it, is what we bring to <a href="/neuroanalytics/">brain-health neuroanalytics</a>.</p>
<p><a href="https://ised-isde.canada.ca/site/innovative-solutions-canada/en/testing-stream" target="_blank" rel="noopener">About the program on canada.ca →</a></p>
""",
        "related": ["innovative-solutions-canada-testing-stream", "technology-readiness-level"],
    },
    {
        "slug": "about",
        "crumb": "About",
        "kicker": "About TextGenetic",
        "title": "About TextGenetic AI Inc. — Kitchener, Ontario",
        "description": "TextGenetic AI Inc. is a federally incorporated Canadian AI company in Kitchener, Ontario, building brain-health neuroanalytics and workflow automation for specialized care.",
        "h1": "Science you can <em class=\"acc\">ship</em>",
        "lead": "TextGenetic AI Inc. is a federally incorporated Canadian company based in Kitchener, Ontario, at the centre of the country's technology corridor. We were founded by engineers and data scientists with research backgrounds, and we build AI the way we'd want it built for our own families: measured, reviewable and private by design.",
        "body": """
<h2>What we do</h2>
<p>We work on two connected fronts. The first is <a href="/health-workflow-automation/">workflow automation for specialized care</a> — replacing lists, paper and memory with one coordinated view of patients, programs and reassessments. The second is <a href="/neuroanalytics/">neuroanalytics</a> — turning clinical signals into neural biomarkers and progression analytics for neurodegenerative disease.</p>

<h2>How we got here</h2>
<p>Our predictive engine was validated first where mistakes are expensive: a municipal fleet. The <a href="/predictive-maintenance-ai/">City of Kitchener pilot</a> ($100,000, Pitch Kitchener) proved the technology in live operations, and the Government of Canada selected it for the <a href="/isc-testing-stream/">ISC Testing Stream</a>. We then applied the same discipline to brain health.</p>

<h2>Principles</h2>
<ul>
  <li><strong>Clinician in the loop.</strong> AI assists; a qualified person always makes the clinical call.</li>
  <li><strong>Privacy by design.</strong> De-identified, governed data foundations ready for research and audit.</li>
  <li><strong>Production first.</strong> Models that hold up outside the lab, in the tools people already use.</li>
</ul>

<h2>Contact</h2>
<p>151 Charles St. W, Kitchener, ON N2G 1H6, Canada · <a href="mailto:info@textgenetic.com">info@textgenetic.com</a> · <a href="/#contact">Contact form</a></p>
""",
        "related": ["clinician-in-the-loop", "de-identification"],
    },
]

GLOSSARY = [
    {
        "slug": "neuroanalytics",
        "term": "Neuroanalytics",
        "short": "The use of data analysis and machine learning on clinical, behavioural and sensor signals to measure and predict brain health over time.",
        "body": """
<p>Neuroanalytics applies statistics and machine learning to signals related to the brain and nervous system — assessment scores, movement and gait measures, speech features, cognitive tests, imaging and medication records — to describe a person's neurological state and how it is changing. Where a single clinic visit gives a snapshot, neuroanalytics works on the trend.</p>
<p>In neurodegenerative disease (Parkinson's, Alzheimer's, mild cognitive impairment), typical goals are to track progression, identify patients who share a trajectory, surface candidate <a href="/glossary/digital-biomarker/">digital biomarkers</a>, and support earlier, better-targeted care and research. The analysis depends on consistent, longitudinal capture: without clean data over time there is nothing to analyse.</p>
""",
        "why": "Neuroanalytics is the second half of our platform: once care workflows produce structured, de-identified records, the same data becomes the basis for progression analytics and biomarker discovery. See <a href=\"/neuroanalytics/\">our neuroanalytics work</a>.",
        "related": ["digital-biomarker", "longitudinal-data", "parkinsons-disease-subtypes"],
    },
    {
        "slug": "digital-biomarker",
        "term": "Digital biomarker",
        "short": "An objective, measurable feature derived from digital data — sensors, devices, software — that reflects a biological or clinical state.",
        "body": """
<p>A biomarker is any measurable indicator of a biological state: blood pressure, a lab value, a score on a scale. A <em>digital</em> biomarker is one computed from data collected through digital means — wearable sensors, a phone's microphone, a gait mat, software that logs how a task is performed. Examples in neurology include stride-length variability from a gait sensor, speech pacing from recorded voice, or reaction-time distributions from a cognitive test on a tablet.</p>
<p>Digital biomarkers are attractive because they can be captured frequently, cheaply and outside the clinic, which makes them well suited to tracking slow change. They are only useful once validated: a candidate feature must be shown to be reliable, to correlate with a clinically meaningful outcome, and to change in a way that matters. Most of the work is in the capture and the validation, not in the model.</p>
""",
        "why": "Our platform captures gait, balance, cognition, speech and medication-response signals longitudinally so that candidate biomarkers can be mined and then validated with clinicians — the foundation of our <a href=\"/neuroanalytics/\">neuroanalytics</a> work.",
        "related": ["neuroanalytics", "freezing-of-gait", "longitudinal-data"],
    },
    {
        "slug": "freezing-of-gait",
        "term": "Freezing of gait",
        "short": "A sudden, brief inability to start or continue walking despite the intention to move, common in advanced Parkinson's disease.",
        "body": """
<p>Freezing of gait (FOG) is an episodic symptom in which a person's feet feel "glued to the floor" for seconds at a time. It often occurs when starting to walk, turning, passing through doorways or approaching a destination, and it is a major cause of falls. FOG is most associated with Parkinson's disease but appears in other parkinsonian conditions too.</p>
<p>Because episodes are brief and situational, FOG is hard to capture in a clinic visit; patients may not experience an episode during the appointment at all. Structured, longitudinal recording — frequency, triggers, duration, relationship to medication timing — is therefore valuable both for care planning and for developing <a href="/glossary/digital-biomarker/">digital biomarkers</a> that can detect or predict episodes.</p>
""",
        "why": "Freezing-of-gait episodes are one of the signals our platform captures over time, alongside gait, balance, cognition and medication response.",
        "related": ["digital-biomarker", "neuroanalytics", "parkinsons-disease-subtypes"],
    },
    {
        "slug": "parkinsons-disease-subtypes",
        "term": "Parkinson's disease subtypes",
        "short": "Groups of people with Parkinson's disease who share a pattern of symptoms, progression rate or underlying biology, used to tailor care and research.",
        "body": """
<p>Parkinson's disease is not one uniform condition. Two people with the same diagnosis can differ widely in their dominant symptoms (tremor versus postural instability and gait difficulty), the speed of progression, the presence of cognitive or mood symptoms, and their response to medication. Subtyping is the attempt to describe these groups systematically.</p>
<p>Historically subtypes were defined by clinicians from motor presentation. Data-driven subtyping instead uses clustering and related methods on clinical, behavioural and biological data to find groups that are stable, clinically meaningful and ideally predictive of progression. Reliable subtypes can improve prognosis conversations, help match patients to the right care pathway, and make clinical trials more efficient by enrolling the people most likely to respond.</p>
""",
        "why": "Identifying clinically meaningful subtypes and reference phenotypes — and predicting which one a patient belongs to — is a core goal of our <a href=\"/neuroanalytics/\">neuroanalytics</a> research.",
        "related": ["neuroanalytics", "longitudinal-data", "digital-biomarker"],
    },
    {
        "slug": "mild-cognitive-impairment",
        "term": "Mild cognitive impairment (MCI)",
        "short": "A measurable decline in memory or thinking that is greater than expected for age but not severe enough to be dementia.",
        "body": """
<p>Mild cognitive impairment describes cognitive change that is noticeable — to the person, to family, and on testing — but does not yet interfere substantially with daily independence. <em>Amnestic</em> MCI primarily affects memory and carries a higher likelihood of progressing to Alzheimer's disease; other forms affect attention, language or executive function.</p>
<p>Not everyone with MCI progresses, and some people remain stable or improve. Predicting who will progress, and how quickly, is one of the central questions in cognitive-health research, and it depends on tracking assessments and other signals over time rather than at a single visit.</p>
""",
        "why": "Alzheimer's disease and amnestic MCI are part of the scope of our progression analytics, alongside Parkinson's disease.",
        "related": ["neuroanalytics", "longitudinal-data"],
    },
    {
        "slug": "longitudinal-data",
        "term": "Longitudinal data",
        "short": "Repeated measurements of the same individuals over time, as opposed to a single snapshot.",
        "body": """
<p>Longitudinal data records the same variables for the same people at multiple points — assessment scores every six months, gait measures every visit, medication changes as they happen. It is the only way to observe change directly: cross-sectional data (one measurement per person) can show that older patients score lower, but not whether a given patient is declining.</p>
<p>Longitudinal data is harder to collect well. Measurements must be consistent across visits and sites, timing must be recorded accurately, and missing visits must be handled honestly. In practice, the quality of a neuroanalytics program is decided by the quality of its longitudinal capture.</p>
""",
        "why": "Our workflow layer exists partly to make longitudinal capture routine: when reassessments are tracked automatically, the data needed for progression analytics accumulates as a by-product of good care.",
        "related": ["neuroanalytics", "reassessment-tracking", "de-identification"],
    },
    {
        "slug": "clinician-in-the-loop",
        "term": "Clinician in the loop",
        "short": "A design principle in which AI assists, drafts and flags, but a qualified clinician reviews and makes every clinical decision.",
        "body": """
<p>"Human in the loop" describes systems where a person reviews or approves what an automated system proposes. "Clinician in the loop" is the healthcare form of the principle: an AI system may draft documentation, suggest a reassessment, or flag a pattern in a patient's data, but the decision to act is taken by a qualified clinician who can see why the suggestion was made and can override it.</p>
<p>The principle matters for safety, for accountability and for adoption. Clinicians rightly distrust tools that act on their behalf without visibility; tools that make their judgment faster and better informed are welcomed. It also shapes system design: suggestions must be explainable, overrides must be easy and logged, and the system must degrade gracefully when the clinician disagrees.</p>
""",
        "why": "Every feature we build follows this line. Our documentation support and assessment assistance are reviewed by clinicians; nothing in the platform makes an autonomous clinical decision.",
        "related": ["care-coordination", "de-identification"],
    },
    {
        "slug": "de-identification",
        "term": "De-identification",
        "short": "Removing or transforming personal identifiers in health data so that individuals cannot reasonably be identified, enabling research use.",
        "body": """
<p>De-identification is the process of stripping direct identifiers (names, health-card numbers, addresses, exact dates) and reducing indirect identifiers (rare combinations of age, location and diagnosis) so that a dataset can be used for analysis and research without exposing the people in it. Techniques range from removing fields and generalizing dates to statistical methods that measure re-identification risk.</p>
<p>In Canada, provincial health-privacy laws such as Ontario's PHIPA and the federal PIPEDA set the expectations for how personal health information is handled; de-identification is what makes "research-ready" data possible while meeting those expectations. It is not a one-time step but an ongoing practice, with governance over who can access what and for which purpose.</p>
""",
        "why": "We build de-identified, governed data foundations from the start so that care data can support research and audit without compromising patients' privacy.",
        "related": ["clinician-in-the-loop", "federated-learning", "longitudinal-data"],
    },
    {
        "slug": "federated-learning",
        "term": "Federated learning",
        "short": "A way of training a machine-learning model across several organizations without moving their raw data to a central place.",
        "body": """
<p>In conventional machine learning, all training data is pooled in one location. In federated learning, the model travels instead: each participating site trains on its own data locally and shares only model updates (weights or gradients), which are aggregated into a shared model. Raw records never leave the site.</p>
<p>The approach suits healthcare, where data is sensitive, governed by different institutions, and often cannot be shared. It lets hospitals or clinics contribute to a common model while keeping custody of their own data. It is not a complete privacy solution on its own — updates can leak information unless additional safeguards are used — but it removes the single biggest barrier: centralizing patient data.</p>
""",
        "why": "Scalable, reproducible analytics across sites is part of how we think about extending our neuroanalytics framework, with federated approaches where they are appropriate and feasible.",
        "related": ["de-identification", "neuroanalytics"],
    },
    {
        "slug": "care-coordination",
        "term": "Care coordination",
        "short": "Organizing a patient's care across providers, programs and sites so that assessments, follow-ups and handoffs happen on time.",
        "body": """
<p>Care coordination is the deliberate organization of patient-care activities among everyone involved — clinicians, programs, sites, families — so that the right things happen in the right order. In specialized care for chronic and neurodegenerative conditions, it means knowing which program each patient is in, when they are due for reassessment, who owns each open follow-up, and what changed since the last visit.</p>
<p>Poor coordination is rarely a failure of individuals; it is the predictable result of information living in separate systems, spreadsheets and memory. The remedy is a shared, current view of each patient's status, with ownership and due dates made explicit.</p>
""",
        "why": "A central care registry with automated reassessment and follow-up tracking is the core of our <a href=\"/health-workflow-automation/\">workflow automation</a> for specialized clinics.",
        "related": ["reassessment-tracking", "clinician-in-the-loop"],
    },
    {
        "slug": "reassessment-tracking",
        "term": "Reassessment tracking",
        "short": "Automatically computing and monitoring when each patient is due for a scheduled clinical reassessment, and who is responsible.",
        "body": """
<p>Many care programs require patients to be reassessed at defined intervals — a cognitive screen every six months, a functional assessment annually, a medication review after any change. Reassessment tracking is the practice of deriving those due dates from program rules and the patient's history, surfacing what is due or overdue, and assigning ownership so nothing waits on someone remembering.</p>
<p>Beyond compliance, consistent reassessment is what makes a patient's record useful over time: each on-schedule assessment is another point on the trend line that progression analytics depends on.</p>
""",
        "why": "Automated reassessment tracking is one of the first things we deliver, because it gives staff time back immediately and builds the longitudinal data that later analytics require.",
        "related": ["care-coordination", "longitudinal-data"],
    },
    {
        "slug": "predictive-maintenance",
        "term": "Predictive maintenance",
        "short": "Using data and machine learning to forecast when equipment is likely to fail, so maintenance happens before the failure instead of after it or on a fixed schedule.",
        "body": """
<p>Traditional maintenance is either <em>reactive</em> (fix it when it breaks) or <em>preventive</em> (service it every N kilometres or months, whether it needs it or not). Predictive maintenance uses the equipment's own history — work orders, sensor and telematics data, usage patterns — to estimate the likelihood of a specific failure in a given window, and schedules work accordingly.</p>
<p>The benefits are fewer unexpected breakdowns, less downtime, longer asset life and lower cost, because healthy assets are not over-serviced and failing ones are caught early. The hard parts are data quality (work orders are messy), choosing a prediction target that crews can act on, and earning trust by being right in a way operators can verify.</p>
""",
        "why": "This is the problem our forecasting engine was first proven on, in the <a href=\"/predictive-maintenance-ai/\">City of Kitchener fleet pilot</a>, before the same discipline was applied to brain health.",
        "related": ["technology-readiness-level", "innovative-solutions-canada-testing-stream"],
    },
    {
        "slug": "technology-readiness-level",
        "term": "Technology Readiness Level (TRL)",
        "short": "A 1-to-9 scale that describes how mature a technology is, from basic principles (TRL 1) to a system proven in real operations (TRL 9).",
        "body": """
<p>Technology Readiness Levels originated at NASA and are now used widely by governments and funders to describe maturity in a consistent way. Roughly: TRL 1–3 cover research and proof of concept; TRL 4–6 cover prototypes validated in the lab and then in a relevant environment; TRL 7–9 cover a system demonstrated in an operational environment, qualified, and finally proven through successful real-world use.</p>
<p>The scale matters for procurement: a buyer testing a TRL 8 system is evaluating something deployable, not funding research. Programs such as the <a href="/glossary/innovative-solutions-canada-testing-stream/">ISC Testing Stream</a> explicitly target TRL 7–9 innovations for that reason.</p>
""",
        "why": "Our selection for the ISC Testing Stream recognizes our platform at TRL 7–9 — late-stage, deployable technology.",
        "related": ["innovative-solutions-canada-testing-stream", "predictive-maintenance"],
    },
    {
        "slug": "innovative-solutions-canada-testing-stream",
        "term": "Innovative Solutions Canada — Testing Stream",
        "short": "A Government of Canada program that procures late-stage Canadian innovations (TRL 7–9) and tests them in real federal operational environments.",
        "body": """
<p>Innovative Solutions Canada (ISC) is a federal program with two streams. The Challenge Stream funds early research and development against problems posed by departments. The Testing Stream is different: it buys pre-commercial, late-stage innovations and has a federal department test them in its own operations, producing an independent evaluation of how the innovation performs.</p>
<p>For a company, selection provides real-world validation from a government user and a pathway to commercialization with the federal government. For departments, it is a way to try Canadian innovations before they are widely available. The program is run by Innovation, Science and Economic Development Canada (ISED); <a href="https://ised-isde.canada.ca/site/innovative-solutions-canada/en/testing-stream" target="_blank" rel="noopener">details are on canada.ca</a>.</p>
""",
        "why": "TextGenetic AI has been <a href=\"/isc-testing-stream/\">selected for the Testing Stream</a>.",
        "related": ["technology-readiness-level", "predictive-maintenance"],
    },
    {
        "slug": "digital-phenotyping",
        "term": "Digital phenotyping",
        "short": "Characterizing a person's health and behaviour from data generated by everyday digital devices, such as phones and wearables.",
        "body": """
<p>A phenotype is the observable set of characteristics of an individual. Digital phenotyping uses passively and actively collected device data — movement from accelerometers, typing speed, voice, sleep patterns, location variability — to describe behaviour and health continuously, in daily life, rather than at scheduled clinical visits.</p>
<p>It overlaps with <a href="/glossary/digital-biomarker/">digital biomarkers</a>: phenotyping is the broad characterization; a biomarker is a specific validated feature within it. Both depend on careful handling of consent and privacy, since the data is intimate and continuous.</p>
""",
        "why": "Longitudinal capture of gait, speech and cognition signals is a clinical form of the same idea, applied within specialized care rather than through consumer devices.",
        "related": ["digital-biomarker", "neuroanalytics", "de-identification"],
    },
]
