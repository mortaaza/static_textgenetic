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
        "slug": "long-term-care",
        "cls": "page--wide",
        "crumb": "ChartDesk",
        "kicker": "Project · Long-term care · ChartDesk · Working prototype",
        "title": "ChartDesk: AI for paper records in long-term care — TextGenetic AI",
        "description": "ChartDesk turns the paper side of a long-term care resident's chart (faxed labs, hospital reports, handwritten notes) into a searchable, source-linked record for the nurse in charge. See what we built, how it works, and try the demo.",
        "h1": "ChartDesk: the paper side of the chart, <em class=\"acc\">finally searchable</em>",
        "lead": "In many long-term care homes, much of a resident's record still lives on paper. Lab results and hospital reports arrive by fax and go into binders; behaviour sheets and notes are written by hand. ChartDesk reads those pages, files them to the right resident, and puts the right information, with its source, in front of the nurse and physician. A working prototype is online today.",
        "body": """
<div class="demo-card">
  <div>
    <h2>Try the working demo</h2>
    <p>Explore ChartDesk with 56 fictional residents and 377 scanned, faxed and handwritten pages. No real resident information is used.</p>
    <a class="btn btn--primary" href="https://chartdesk.textgenetic.com" target="_blank" rel="noopener">Open the demo &rarr;</a>
    <a class="btn btn--ghost-light" href="/long-term-care/demo/">Step-by-step guide</a>
  </div>
  <div class="creds-box">
    <div><span>Username</span><b>demo</b></div>
    <div><span>Password</span><b>demo</b></div>
    <small>Works on a computer, tablet or phone.</small>
  </div>
</div>

<h2>Who it is for</h2>
<p>Older adults living in long-term care, many of them living with dementia, and the people who care for them: the nurse in charge, the attending physician or nurse practitioner, and the office staff who handle referrals and transfers. Every resident deserves care informed by their whole story, including the parts that are still on paper.</p>

<h2>What we observed</h2>
<p>In October 2026 we spent three days on site with a long-term care team in Ontario and the office of its attending physician. We sat with the nursing and administration desk, the reception team, the physician during his weekly round workflow, and the clinic staff who manage referrals. What we observed:</p>
<ul>
  <li><strong>Finding information takes much of the day.</strong> As one team member put it, <em>"We're wasting so much time to look for things."</em> Faxed lab results are filed on paper in the chart, not scanned.</li>
  <li><strong>Results are retyped.</strong> When a result needs action, staff search the chart for the latest related values and type them into a message for the physician.</li>
  <li><strong>Doctor days run on paper.</strong> A week of concerns and handwritten behaviour sheets are gathered for the physician to review, sign and file.</li>
  <li><strong>Referrals and transfers are assembled by hand,</strong> with a different form for each destination: 5 to 10 minutes each, if nobody interrupts.</li>
  <li><strong>Follow-ups are hard to track,</strong> because they sit inside progress notes and outside reports.</li>
  <li><strong>The same information is entered several times</strong> across separate systems and paper.</li>
</ul>
<p>When information is fragmented, care coordination becomes harder, and the risk of missed information and delayed care goes up.</p>

<h2>What we built</h2>
<p>A working web application, built in November 2026 directly from those observations, and tested on realistic records we created for the purpose.</p>
<div class="stat-row">
  <div><strong>56</strong><span>fictional residents, each with a full paper history</span></div>
  <div><strong>377</strong><span>page images: faxes, photocopies, forms and handwriting</span></div>
  <div><strong>97.7%</strong><span>of words read correctly from the page images</span></div>
  <div><strong>962 / 962</strong><span>lab values and every resident name read correctly</span></div>
</div>
<p class="small" style="font-size:.88rem">Measured on our own test pages, degraded to look faxed and photocopied. Real-world accuracy will be measured with partner homes.</p>

<figure class="shot"><img src="/assets/chartdesk/1-inbox.jpg" alt="ChartDesk fax and scan inbox: a faxed clinic note beside the resident ChartDesk suggests" loading="lazy" width="1920" height="1200"></figure>
<figcaption>The fax and scan inbox. ChartDesk reads the page, finds the name and date of birth, and suggests the resident; here it flags a misspelled name. A nurse confirms.</figcaption>

<ul>
  <li><strong>Capture and file.</strong> Faxes, scans and phone photos are read and matched to the right resident by name and date of birth. A nurse confirms with one tap; nothing is filed on its own.</li>
  <li><strong>Two views of every record.</strong> An exact copy of every original page, and an electronic chart organized by importance: goals of care first, then results, follow-ups and documents.</li>
  <li><strong>Find.</strong> Ask in plain words. The answer cites the exact page it came from; if the record does not say, ChartDesk answers "Not found in the record" instead of guessing.</li>
  <li><strong>Due and overdue.</strong> Follow-ups written inside reports, such as "repeat potassium in 48 to 72 hours", become a visible due list.</li>
  <li><strong>Doctor-day pack.</strong> Before the physician's round: what changed this week for each resident, with sources, and who has nothing new.</li>
  <li><strong>Referrals and transfers.</strong> The nurse writes the reason; ChartDesk adds goals of care, history, medications, allergies and recent results, then tracks whether the referral was received.</li>
  <li><strong>Change in condition.</strong> Drafts an <a href="/glossary/sbar/">SBAR</a> for the physician with <a href="/glossary/goals-of-care/">goals of care</a> shown first, to help avoid unnecessary hospital transfers.</li>
  <li><strong>Behaviour trends.</strong> Handwritten behaviour observation sheets become an hour-by-hour pattern the team can see.</li>
  <li><strong>Activity log.</strong> Every sign-in, search, chart view, filing and approval is recorded.</li>
</ul>

<figure class="shot"><img src="/assets/chartdesk/3-original.jpg" alt="An original faxed lab report shown beside the text ChartDesk read from it" loading="lazy" width="1920" height="1200"></figure>
<figcaption>Explainable by design: every page can be opened beside what ChartDesk read from it, and read again live.</figcaption>

<h2>How it works</h2>
<ol class="timeline">
  <li><b>Read.</b> A vision model reads each page image, including faxes, photocopies and handwriting, and keeps the text exactly as written.</li>
  <li><b>Match.</b> Name and date of birth are compared with the resident list. A one-letter misspelling is flagged for checking; a page for someone who does not live in the home is not matched.</li>
  <li><b>Extract.</b> Lab values and follow-up instructions are pulled into the chart, each linked to its line on the original page.</li>
  <li><b>Find and draft.</b> Search ranks the matching pages; the assistant answers only from those pages and cites them. Drafts (SBAR, referral, round pack) use only facts from the chart.</li>
  <li><b>Approve.</b> A nurse or physician reviews every filing and draft before it reaches the chart. ChartDesk does not diagnose or suggest treatment.</li>
</ol>

<h2>People stay in charge</h2>
<p>ChartDesk organizes, finds and drafts. It does not make clinical decisions. Every draft is reviewed by a nurse or physician before it reaches the chart, in line with our <a href="/glossary/clinician-in-the-loop/">clinician-in-the-loop</a> principle.</p>

<h2>Privacy by design</h2>
<ul>
  <li>Designed for Ontario's PHIPA and Canada's PIPEDA. The home remains the custodian of resident information; we act only as its agent under a written agreement.</li>
  <li>No resident data is used until a privacy agreement and privacy impact assessment are in place.</li>
  <li>Before any resident information is used, it will be stored and processed in Canada, encrypted and access-logged. It is never used to train AI models.</li>
  <li>Research and development use realistic test records, not real resident data. The demo contains fictional people only.</li>
</ul>

<h2>Timeline</h2>
<ol class="timeline">
  <li><b>October 2026.</b> Three days of on-site discovery with a long-term care team and its attending physician's office.</li>
  <li><b>November 2026.</b> Working prototype online, tested on 377 realistic page images; doctor-day pack, referral package and photo upload added from what the team asked for.</li>
  <li><b>Next.</b> Test with nurses and physicians on realistic records, measure time saved finding and filing, then pilot in Ontario homes once privacy agreements are in place.</li>
</ol>
""",
        "cta": ("Run a long-term care home in Ontario?", "We'd like to learn how paper and faxes work in your home, and explore testing ChartDesk with your team. No resident data is involved until privacy agreements are in place."),
        "related": ["sbar", "goals-of-care", "clinician-in-the-loop", "care-coordination"],
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
<p>We work on two connected fronts. The first is <a href="/health-workflow-automation/">workflow automation for specialized care</a> — replacing lists, paper and memory with one coordinated view of patients, programs and reassessments. The second is <a href="/neuroanalytics/">neuroanalytics</a> — turning clinical signals into neural biomarkers and progression analytics for neurodegenerative disease. We are also building <a href="/long-term-care/">ChartDesk</a>, which makes the paper side of a long-term care resident's chart searchable for the nurse in charge.</p>

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
    {
        "slug": "sbar",
        "term": "SBAR",
        "short": "Situation, Background, Assessment, Recommendation: a standard structure nurses use to tell a physician about a change in a patient's condition.",
        "body": """
<p>SBAR is a short, structured way to communicate a clinical concern, widely used in hospitals and long-term care. The <strong>Situation</strong> says what is happening now; the <strong>Background</strong> gives the relevant history, medications and recent results; the <strong>Assessment</strong> is the nurse's view of what is going on; and the <strong>Recommendation</strong> (or Request) states what the nurse is asking for.</p>
<p>A good SBAR depends on having the right facts at hand: the latest lab results, recent hospital notes and the resident's <a href="/glossary/goals-of-care/">goals of care</a>. When those live on paper, assembling them during an evening call is slow and error-prone.</p>
""",
        "why": "<a href=\"/long-term-care/\">ChartDesk</a> drafts an SBAR from the resident's record, with sources linked and goals of care shown first, for the nurse to review and send.",
        "related": ["goals-of-care", "clinician-in-the-loop"],
    },
    {
        "slug": "goals-of-care",
        "term": "Goals of care",
        "short": "A resident's documented wishes and agreed plan for the kind of care they want, including whether a hospital transfer fits those wishes.",
        "body": """
<p>Goals of care describe what matters most to a person and the level of treatment they want, agreed through conversation with the person or their substitute decision-maker and the care team. In long-term care, they often guide decisions such as whether to treat a problem in the home or transfer the resident to hospital.</p>
<p>These wishes only help if they are visible at the moment a decision is made. Surfacing them first, before the clinical details, keeps urgent decisions aligned with what the resident wants.</p>
""",
        "why": "When a resident's condition changes, <a href=\"/long-term-care/\">ChartDesk</a> shows goals of care at the top of the SBAR draft, to help avoid transfers the resident would not want.",
        "related": ["sbar", "care-coordination"],
    },
]


# ---- Extra pages: rendered by build_pages.py ---------------------------------
PAGES = [
    {
        "path": "/long-term-care/demo/",
        "cls": "page--wide",
        "crumbs": [("ChartDesk", "/long-term-care/"), ("Demo guide", "/long-term-care/demo/")],
        "kicker": "ChartDesk · Demo guide",
        "title": "Try the ChartDesk demo: a step-by-step guide — TextGenetic AI",
        "description": "How to open and explore the ChartDesk demo for long-term care: sign in with demo / demo, then follow eight short steps through the inbox, charts, search, doctor-day pack, referrals and SBAR drafts. Fictional records only.",
        "h1": "Try the ChartDesk demo, <em class=\"acc\">step by step</em>",
        "lead": "The demo is a working copy of ChartDesk for a fictional long-term care home with two units, 56 residents and 377 scanned, faxed and handwritten pages. Everything you see is fictional. It takes about ten minutes to try every part.",
        "body": """
<div class="demo-card">
  <div>
    <h2>Open the demo</h2>
    <p>It opens in a new tab. Sign in with the details on the right.</p>
    <a class="btn btn--primary" href="https://chartdesk.textgenetic.com" target="_blank" rel="noopener">Open ChartDesk &rarr;</a>
  </div>
  <div class="creds-box">
    <div><span>Address</span><b>chartdesk.textgenetic.com</b></div>
    <div><span>Username</span><b>demo</b></div>
    <div><span>Password</span><b>demo</b></div>
  </div>
</div>

<h2>Before you start</h2>
<ul>
  <li><strong>Every resident and record is fictional.</strong> Names, faces and pages were generated for testing. Never add a page about a real person.</li>
  <li><strong>The demo is shared.</strong> Other visitors may be trying it at the same time. <b>Reset demo data</b>, at the bottom of the menu, puts everything back to the start.</li>
  <li><strong>The demo date is fixed</strong> at November 22, 2026, so dates on the pages and the due list always agree.</li>
  <li><strong>Use any device.</strong> On a phone, the menu is behind the button at the top left.</li>
</ul>

<h2>A ten-minute tour</h2>
<ol class="tour">
  <li>
    <div class="tour__text"><h3>Fax and scan inbox</h3><p>Every new page waits here. ChartDesk shows the page image, what it read, the resident it suggests and any follow-up it found. Nothing is filed until a nurse confirms.</p><p class="try"><b>Try it:</b> Open the <b>Consult note</b> from the anticoagulation clinic: the name on the page is misspelled, and ChartDesk flags it as a <b>close spelling</b>. Then try a <b>Handwritten</b> note, and press <b>Confirm &amp; file</b>. To add your own page, use <b>Choose photo or scan</b> with a fictional page only.</p></div>
    <figure class="shot"><img src="/assets/chartdesk/1-inbox.jpg" alt="ChartDesk demo: Fax and scan inbox" loading="lazy" width="1920" height="1200"></figure>
  </li>
  <li>
    <div class="tour__text"><h3>A resident's chart</h3><p>Each resident has one chart organized by importance: goals of care first, then lab trends, documents, follow-ups, medications, and the family doctor and pharmacy from before admission.</p><p class="try"><b>Try it:</b> Go to <b>Residents</b> and open <b>Margaret Ellis</b>. Each lab value has a <b>source</b> link.</p></div>
    <figure class="shot"><img src="/assets/chartdesk/2-chart.jpg" alt="ChartDesk demo: A resident's chart" loading="lazy" width="1920" height="1200"></figure>
  </li>
  <li>
    <div class="tour__text"><h3>The original page, beside what was read</h3><p>Every document can be opened beside the text ChartDesk read from it, so anyone can check it. <b>Read again, live</b> sends the image to the page reader in front of you.</p><p class="try"><b>Try it:</b> In Margaret Ellis's chart, click any document under <b>Documents</b>, then <b>Read again, live</b>.</p></div>
    <figure class="shot"><img src="/assets/chartdesk/3-original.jpg" alt="ChartDesk demo: The original page, beside what was read" loading="lazy" width="1920" height="1200"></figure>
  </li>
  <li>
    <div class="tour__text"><h3>Find: ask in plain words</h3><p>Search every filed page by exact words or in plain language. The answer cites the pages it used; each citation opens the original with the words highlighted.</p><p class="try"><b>Try it:</b> Click a suggested question, or ask <b>Who had a high INR?</b> Then ask something the record does not contain: ChartDesk answers <b>Not found in the record</b> instead of guessing.</p></div>
    <figure class="shot"><img src="/assets/chartdesk/4-find.jpg" alt="ChartDesk demo: Find: ask in plain words" loading="lazy" width="1920" height="1200"></figure>
  </li>
  <li>
    <div class="tour__text"><h3>Doctor day</h3><p>A pack for the physician's weekly round: for each resident, this week's nursing notes, results that are newly out of range or getting worse, new outside reports and what is due, each with its source. Residents with nothing new are listed separately.</p><p class="try"><b>Try it:</b> Mark a resident <b>Seen, no change</b>, filter by unit, or press <b>Print pack</b>.</p></div>
    <figure class="shot"><img src="/assets/chartdesk/5-doctor-day.jpg" alt="ChartDesk demo: Doctor day" loading="lazy" width="1920" height="1200"></figure>
  </li>
  <li>
    <div class="tour__text"><h3>Referrals and transfers</h3><p>The nurse writes the reason in their own words; ChartDesk gathers goals of care, history, medications and allergies, the latest results and the pre-admission family doctor and pharmacy, each with its source.</p><p class="try"><b>Try it:</b> Press <b>Build package</b> with the example filled in. Try a vague reason such as &ldquo;knee pain&rdquo;: it is refused. <b>Approve &amp; save</b> adds a follow-up to confirm the referral arrived.</p></div>
    <figure class="shot"><img src="/assets/chartdesk/6-referral.jpg" alt="ChartDesk demo: Referrals and transfers" loading="lazy" width="1920" height="1200"></figure>
  </li>
  <li>
    <div class="tour__text"><h3>Change in condition</h3><p>When a resident's condition changes, ChartDesk drafts an SBAR for the physician from the nurse's own words and the chart, with goals of care shown first. It does not diagnose or suggest orders.</p><p class="try"><b>Try it:</b> Press <b>Draft SBAR</b>, edit any section, then <b>Approve &amp; save to chart</b>. The saved note appears in the resident's documents.</p></div>
    <figure class="shot"><img src="/assets/chartdesk/7-sbar.jpg" alt="ChartDesk demo: Change in condition" loading="lazy" width="1920" height="1200"></figure>
  </li>
  <li>
    <div class="tour__text"><h3>Behaviour trends</h3><p>Seven days of handwritten behaviour observation sheets become an hour-by-hour grid, with simple counts of when responsive behaviours happen.</p><p class="try"><b>Try it:</b> Choose different residents from the list to compare patterns.</p></div>
    <figure class="shot"><img src="/assets/chartdesk/8-behaviour.jpg" alt="ChartDesk demo: Behaviour trends" loading="lazy" width="1920" height="1200"></figure>
  </li>
</ol>

<h2>What the demo does not do yet</h2>
<ul>
  <li>Pages are added by upload or come preloaded. In a home, the fax line and scanner would feed the inbox directly.</li>
  <li>It is not connected to an electronic health record or pharmacy system.</li>
  <li>The demo has one shared login. A real deployment has a named account and role for each person.</li>
</ul>
""",
        "cta": ("Want a guided walkthrough?", "We are happy to show ChartDesk to your team, and to hear how paper and faxes work in your home."),
    },
    {
        "path": "/projects/",
        "crumbs": [("Projects", "/projects/")],
        "kicker": "Our work",
        "title": "Projects — TextGenetic AI",
        "description": "TextGenetic AI projects: ChartDesk for long-term care records, a care coordination and neuroanalytics platform, and the City of Kitchener predictive maintenance pilot.",
        "h1": "Projects: <em class=\"acc\">what we have built</em>",
        "lead": "Each project starts with time on site with the people who do the work, then a working system tested on realistic data, then a measured pilot.",
        "cls": "page--wide",
        "body": """
<div class="proj-list">
  <article class="proj-item proj-item--feature">
    <span class="badge" style="background:rgba(255,255,255,.14);color:#fff">Long-term care · Working prototype · 2026</span>
    <h2>ChartDesk: AI for paper records in long-term care</h2>
    <p>Reads the faxes, scans and handwritten pages a long-term care home receives, files each to the right resident, and gives nurses and physicians answers with their source. Built from three days of on-site discovery; tested on 377 realistic page images, with every lab value read correctly.</p>
    <div class="links"><a href="/long-term-care/">Project details &rarr;</a><a href="/long-term-care/demo/">Demo guide &rarr;</a><a href="https://chartdesk.textgenetic.com" target="_blank" rel="noopener">Open the demo &rarr;</a></div>
  </article>
  <article class="proj-item">
    <span class="badge">Healthcare · Flagship</span>
    <h2>Care coordination and neuroanalytics platform</h2>
    <p>For a multi-site neurodegenerative-care provider: a central care registry with automated reassessment and follow-up tracking, longitudinal capture of gait, balance, cognition and medication response, and AI-assisted documentation with clinician review. Client details withheld for confidentiality.</p>
    <div class="links"><a href="/health-workflow-automation/">Workflow automation &rarr;</a><a href="/neuroanalytics/">Neuroanalytics &rarr;</a></div>
  </article>
  <article class="proj-item">
    <span class="badge">Municipal · 2025</span>
    <h2>City of Kitchener: AI fleet analytics pilot</h2>
    <p>Chosen as 1 of 3 companies from 10 finalists at Communitech's Fast Track Cities for a $100,000 pilot: predictive maintenance that flags issues before breakdowns. Now productized as Axion Fleet, and selected for Innovative Solutions Canada's Testing Stream.</p>
    <div class="links"><a href="/predictive-maintenance-ai/">Case study &rarr;</a><a href="/isc-testing-stream/">ISC selection &rarr;</a></div>
  </article>
</div>
""",
        "cta": ("Have a problem like these?", "Tell us about it. We usually start with a short session on site and a scoped pilot on realistic data."),
    },
]
