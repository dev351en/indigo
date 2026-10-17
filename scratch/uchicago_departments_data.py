"""
Comprehensive UChicago Departments and Faculty Data Repository
Contains complete metadata and faculty rosters for all major UChicago departments.
"""

DEPARTMENTS = [
    {
        "id": "department-of-computer-science",
        "slug": "department-of-computer-science",
        "name": "Department of Computer Science",
        "division": "Physical Sciences Division",
        "division_slug": "psd",
        "building": "John Crerar Science Building",
        "address": "5730 S. Ellis Ave, Chicago, IL 60637",
        "chair": "Prof. Michael J. Franklin",
        "tagline": "Pioneering the Foundations of Computing, AI, Systems, and Quantum Information",
        "hero_image": "../assets/subpage_media/data-science-professor.jpg",
        "description": "The Department of Computer Science at the University of Chicago is an epicenter for cutting-edge computing research. Situated in the John Crerar Science Building, our department bridges foundational theoretical computer science with high-impact systems, human-computer interaction, privacy, trustworthy AI, and quantum architectures in close collaboration with Argonne National Laboratory and the Chicago Quantum Exchange.",
        "highlights": [
            "Home to the Data Science Institute (DSI) and the Chicago Quantum Exchange",
            "Pioneered foundational research in computer security, cloud systems, and privacy (e.g. Fawkes, Nightshade)",
            "World-leading faculty in quantum computer architecture and machine learning theory",
            "Comprehensive undergraduate, Master's (MPCS), and Ph.D. degree curricula with full doctoral fellowship support"
        ],
        "undergrad_program": "The Undergraduate Program in Computer Science offers B.S. and B.A. degrees, providing a rigorous grounding in algorithms, programming languages, computer systems, and theoretical foundations, alongside advanced electives in machine learning, graphics, cryptography, and human-computer interaction.",
        "masters_program": "The Master of Science in Computer Science (MPCS) and MS in Computational Analysis and Public Policy (MSCAPP) offer tailored, career-defining curricula for emerging software leaders, systems engineers, and computational policymakers.",
        "phd_program": "The Doctor of Philosophy (Ph.D.) in Computer Science prepares scholars for leadership in academia and industrial research. Doctoral students conduct groundbreaking research from quarter one, supported by comprehensive 5-year funding covering tuition, stipend, and medical insurance.",
        "research_areas": [
            {"title": "Artificial Intelligence & Machine Learning", "desc": "Foundations of deep learning, trustworthy AI, computer vision, natural language processing, and multi-agent coordination."},
            {"title": "Systems, Networks & Architecture", "desc": "Cloud computing, storage architectures, scalable distributed computing, distributed tracing, and resilient hardware design."},
            {"title": "Quantum Computing & Information", "desc": "Quantum software, architectural co-design, error mitigation, and quantum networking in partnership with the Chicago Quantum Exchange."},
            {"title": "Security, Privacy & Society", "desc": "Adversarial machine learning, biometric privacy protection, usable security, cryptography, and surveillance mitigation."},
            {"title": "Theory & Algorithms", "desc": "Computational complexity, spectral graph theory, approximation algorithms, quantum algorithms, and algorithmic game theory."},
            {"title": "Human-Computer Interaction (HCI)", "desc": "Haptic computing, wearable devices, interactive AI interfaces, accessible technologies, and digital fabrication."}
        ],
        "facilities": [
            "John Crerar Science Building high-performance compute clusters and GPU farms",
            "Center for Data and Computing (CDAC) discovery incubators",
            "Chicago Quantum Exchange testbeds and cryogenic laboratories",
            "Human-Computer Integration Lab & Actuated Experience Research Lab"
        ],
        "events": [
            {"title": "Distinguished Computer Science Colloquium", "speaker": "Prof. Fred Chong", "date": "Every Wednesday at 3:30 PM", "loc": "Crerar 390"},
            {"title": "AI & Systems Seminar Series", "speaker": "Invited Researchers from Industry & Academia", "date": "Bi-weekly Thursdays", "loc": "Crerar 298"},
            {"title": "Theory of Computing Seminar", "speaker": "Faculty & Postdoctoral Fellows", "date": "Tuesdays at 11:00 AM", "loc": "Ryerson 251"}
        ],
        "contact": {
            "phone": "(773) 702-6614",
            "email": "cs-admissions@uchicago.asia",
            "office": "John Crerar Science Building, Room 220"
        }
    },
    {
        "id": "department-of-economics",
        "slug": "department-of-economics",
        "name": "Kenneth C. Griffin Department of Economics",
        "division": "Social Sciences Division",
        "division_slug": "ssd",
        "building": "Saieh Hall for Economics",
        "address": "5757 S. University Ave, Chicago, IL 60637",
        "chair": "Prof. Robert Shimer",
        "tagline": "The Birthplace of the Chicago School: Rigorous Empirical and Theoretical Inquiry",
        "hero_image": "../assets/subpage_media/mainquadfall.png",
        "description": "The Kenneth C. Griffin Department of Economics at the University of Chicago is world-renowned for defining modern economic thought. With 30+ Nobel laureates affiliated as faculty, students, or researchers, the 'Chicago School' revolutionized price theory, human capital, monetary policy, behavioral economics, and empirical microeconometrics.",
        "highlights": [
            "30+ Nobel Laureates in Economic Sciences affiliated with UChicago",
            "Pioneered modern Price Theory, Rational Expectations, and Experimental Economics",
            "Home to the Becker Friedman Institute for Economics (BFI) and the Center for the Economics of Human Development",
            "State-of-the-art academic home in the beautifully restored historic Saieh Hall for Economics"
        ],
        "undergrad_program": "The Undergraduate Program in Economics is one of the most prestigious in the world, offering both standard and empirical/data-intensive tracks. Students learn foundational price theory, econometrics, and game theory directly from Nobel laureates and leading economic researchers.",
        "masters_program": "The Department offers joint-degree options, including the Master of Arts Program in the Social Sciences (MAPSS) with Economics concentration, and dual credentials with Chicago Booth and the Harris School of Public Policy.",
        "phd_program": "The Ph.D. in Economics at UChicago is an intensive, internationally celebrated program producing scholars who shape academic institutions, central banks, and international policymaking. Students receive full multi-year financial fellowship packages.",
        "research_areas": [
            {"title": "Price Theory & Applied Microeconomics", "desc": "Foundational price determination, industrial organization, market design, and competitive equilibrium."},
            {"title": "Macroeconomics & Monetary Policy", "desc": "Search and matching models, macroeconomic dynamics, financial frictions, central banking, and international finance."},
            {"title": "Econometrics & Quantitative Methods", "desc": "Non-parametric econometrics, treatment effect evaluation, high-dimensional estimation, and machine learning in economic models."},
            {"title": "Human Capital & Development", "desc": "Early childhood intervention, education economics, labor market mobility, and inequality dynamics pioneered by James Heckman."},
            {"title": "Behavioral & Experimental Economics", "desc": "Field experiments, social preferences, behavioral nudges, and public goods mechanisms pioneered by John List and Richard Thaler."}
        ],
        "facilities": [
            "Saieh Hall for Economics state-of-the-art lecture auditoriums and research suites",
            "Becker Friedman Institute for Economics (BFI) convening spaces",
            "Center for the Economics of Human Development (CEHD) research laboratories",
            "Experimental Economics Observation and Behavioral Lab"
        ],
        "events": [
            {"title": "Money and Banking Workshop", "speaker": "Prof. Robert Shimer & Guests", "date": "Tuesdays at 12:30 PM", "loc": "Saieh Hall 112"},
            {"title": "Economic Theory & Price Theory Seminar", "speaker": "Visiting Scholars & Faculty", "date": "Thursdays at 3:30 PM", "loc": "Saieh Hall 203"},
            {"title": "Applied Microeconomics Workshop", "speaker": "Prof. James Heckman & Invited Fellows", "date": "Mondays at 1:30 PM", "loc": "Saieh Hall 247"}
        ],
        "contact": {
            "phone": "(773) 702-8260",
            "email": "econ-info@uchicago.asia",
            "office": "Saieh Hall for Economics, Room 102"
        }
    },
    {
        "id": "department-of-physics",
        "slug": "department-of-physics",
        "name": "Department of Physics",
        "division": "Physical Sciences Division",
        "division_slug": "psd",
        "building": "Michelson Center for Physics",
        "address": "929 E. 57th St, Chicago, IL 60637",
        "chair": "Prof. Young-Kee Kim",
        "tagline": "Carrying Forward the Legacy of Fermi, Michelson, and Chandrasekhar",
        "hero_image": "../assets/subpage_media/cosmic-rays-field-experiment.jpg",
        "description": "The Department of Physics at the University of Chicago is one of the most storied institutions in the history of science. From Albert Michelson's pioneering speed-of-light measurements to Enrico Fermi's first controlled nuclear chain reaction (Chicago Pile-1), UChicago physicists have repeatedly reshaped our understanding of the universe across high-energy particle physics, theoretical cosmology, condensed matter, and quantum optics.",
        "highlights": [
            "30 Nobel Laureates in Physics affiliated with the department",
            "Historic home to Enrico Fermi, Albert Michelson, Subrahmanyan Chandrasekhar, and James Cronin",
            "Direct leadership in major international experiments: CERN (ATLAS), Fermilab (DUNE), South Pole Telescope, and James Webb Space Telescope",
            "Close affiliation with the Enrico Fermi Institute (EFI) and James Franck Institute (JFI)"
        ],
        "undergrad_program": "The Undergraduate Program in Physics offers comprehensive B.A. and B.S. degrees characterized by intense mathematical rigor, hands-on advanced laboratory training, and opportunities to join experimental or theoretical research groups as early as freshman year.",
        "masters_program": "The department participates in MS-level research initiatives and joint master's concentrations with Physical Sciences Division divisions.",
        "phd_program": "The Ph.D. in Physics offers rigorous training in theoretical, experimental, and observational physics. All admitted doctoral students receive comprehensive multi-year financial awards including full tuition, competitive living stipend, and health insurance.",
        "research_areas": [
            {"title": "Particle Physics & Fields", "desc": "Collider experiments at CERN LHC, neutrino oscillations with Fermilab DUNE, dark matter detection, and fundamental quantum field theory."},
            {"title": "Astrophysics & Cosmology", "desc": "Cosmic microwave background observations (South Pole Telescope), dark energy surveys, cosmic ray physics, and cosmological evolution."},
            {"title": "Condensed Matter & Materials Physics", "desc": "Quantum materials, high-temperature superconductivity, topological insulators, non-equilibrium systems, and soft matter."},
            {"title": "Atomic, Molecular & Optical (AMO) Physics", "desc": "Ultracold quantum gases, optical lattices, Bose-Einstein condensation, quantum simulation, and precision measurement."},
            {"title": "Theoretical Physics & String Theory", "desc": "Quantum gravity, holographic duality (AdS/CFT), strongly coupled quantum fluids, and relativistic hydrodynamics."}
        ],
        "facilities": [
            "Michelson Center for Physics advanced cleanrooms and optics laboratories",
            "Enrico Fermi Institute (EFI) machine shops and radiation detectors",
            "James Franck Institute (JFI) low-temperature cryostat facilities",
            "Fermilab and Argonne National Laboratory high-energy beamlines"
        ],
        "events": [
            {"title": "Physics Department Colloquium", "speaker": "Distinguished International Speakers", "date": "Thursdays at 4:00 PM", "loc": "Kersten Physics Teaching Center 106"},
            {"title": "EFI Particle & Cosmology Seminar", "speaker": "Prof. Dam Thanh Son & Guests", "date": "Mondays at 3:00 PM", "loc": "Eckhardt 570"},
            {"title": "Condensed Matter & AMO Physics Seminar", "speaker": "Prof. Cheng Chin & Faculty", "date": "Fridays at 1:30 PM", "loc": "Michelson 210"}
        ],
        "contact": {
            "phone": "(773) 702-7006",
            "email": "physics-dept@uchicago.asia",
            "office": "Michelson Center for Physics, Room 108"
        }
    },
    {
        "id": "department-of-mathematics",
        "slug": "department-of-mathematics",
        "name": "Department of Mathematics",
        "division": "Physical Sciences Division",
        "division_slug": "psd",
        "building": "Eckhart Hall",
        "address": "5734 S. University Ave, Chicago, IL 60637",
        "chair": "Prof. Kevin Corlette",
        "tagline": "Pure Mathematical Brilliance in the Heart of Hyde Park",
        "hero_image": "../assets/subpage_media/equation-inside-the-lab.jpg",
        "description": "The Department of Mathematics at the University of Chicago is world-renowned for deep, transformative research in pure mathematics. Housed in the collegiate Gothic beauty of Eckhart Hall, our faculty and researchers have produced foundational breakthroughs in algebraic geometry, number theory, algebraic topology, geometric group theory, and partial differential equations.",
        "highlights": [
            "Fields Medalists including Prof. Ngô Bảo Châu and historical faculty such as Paul Cohen",
            "World-leading center for the Langlands Program and arithmetic geometry",
            "Historic birthplace of modern algebraic topology and Category Theory (Saunders Mac Lane)",
            "Vibrant undergraduate and doctoral communities with renowned Putnam and research mentoring traditions"
        ],
        "undergrad_program": "The Undergraduate Program in Mathematics offers B.A. and B.S. degrees, renowned for its challenging Honors Analysis sequence and advanced courses in abstract algebra, topology, differential geometry, and complex variables.",
        "masters_program": "Joint programs and advanced standing pathways for specialized research in pure and applied mathematics.",
        "phd_program": "The Ph.D. in Mathematics is one of the world's most sought-after programs, immersing doctoral candidates in active mathematical discovery under the mentorship of internationally prominent mathematicians, fully funded with tuition and living fellowships.",
        "research_areas": [
            {"title": "Algebraic Geometry & Number Theory", "desc": "Automorphic forms, Galois representations, p-adic geometry, the Langlands program, and modular forms."},
            {"title": "Algebraic & Differential Topology", "desc": "Homotopy theory, operads, characteristic classes, low-dimensional manifold topology, and knot invariants."},
            {"title": "Geometric Group Theory & Dynamics", "desc": "Mapping class groups, Teichmüller theory, hyperbolic geometry, ergodic theory, and smooth dynamical systems."},
            {"title": "Partial Differential Equations & Analysis", "desc": "Dispersive equations, non-linear harmonic analysis, geometric measure theory, and fluid dynamics."},
            {"title": "Mathematical Logic & Set Theory", "desc": "Model theory, classification theory, computability, and the foundations of infinite mathematics."}
        ],
        "facilities": [
            "Eckhart Hall historic mathematical research library and seminar rooms",
            "Institute for Mathematical and Statistical Innovation (IMSI)",
            "Stevanovich Center for Financial Mathematics",
            "Graduate Student Collaborative Suites and Discussion Commons"
        ],
        "events": [
            {"title": "Mathematics Department Colloquium", "speaker": "Distinguished Visiting Mathematicians", "date": "Fridays at 4:00 PM", "loc": "Eckhart Hall 202"},
            {"title": "Number Theory Seminar", "speaker": "Prof. Ngô Bảo Châu & Prof. Frank Calegari", "date": "Tuesdays at 3:30 PM", "loc": "Eckhart Hall 207"},
            {"title": "Topology & Geometry Seminar", "speaker": "Prof. Benson Farb & Prof. Peter May", "date": "Thursdays at 4:00 PM", "loc": "Eckhart Hall 203"}
        ],
        "contact": {
            "phone": "(773) 702-7100",
            "email": "math-info@uchicago.asia",
            "office": "Eckhart Hall, Room 108"
        }
    },
    {
        "id": "department-of-statistics",
        "slug": "department-of-statistics",
        "name": "Department of Statistics & Data Science",
        "division": "Physical Sciences Division",
        "division_slug": "psd",
        "building": "Jones Laboratory",
        "address": "5747 S. Ellis Ave, Chicago, IL 60637",
        "chair": "Prof. Dan Nicolae",
        "tagline": "Inferential Rigor, Statistical Machine Learning, and Big Data Foundations",
        "hero_image": "../assets/subpage_media/data-science-professor.jpg",
        "description": "The Department of Statistics at the University of Chicago is a global leader in foundational statistical theory, high-dimensional data analysis, statistical machine learning, biostatistics, and statistical genetics. Situated in Jones Laboratory, the department drives the theoretical engines behind modern data science in collaboration with the Data Science Institute.",
        "highlights": [
            "Pioneered foundational generalized linear models (Peter McCullagh) and history of statistics (Stephen Stigler)",
            "MacArthur Fellowship awardees and leaders in distribution-free predictive inference and conformal prediction",
            "Joint degree programs in Data Science, Machine Learning, and Computational Finance",
            "Close partnerships with the Data Science Institute, Argonne National Laboratory, and Biological Sciences Division"
        ],
        "undergrad_program": "Undergraduate B.A. and B.S. degrees in Statistics and Data Science providing deep training in probability, mathematical statistics, computational modeling, and modern machine learning.",
        "masters_program": "The Master of Science in Statistics (MSS) and MS in Financial Mathematics offer intensive computational and theoretical training for top data science, quantitative finance, and doctoral careers.",
        "phd_program": "The Ph.D. in Statistics trains scholars who develop new mathematical frameworks and statistical methodologies for high-dimensional inference, bioinformatics, and machine learning, supported by comprehensive multi-year funding.",
        "research_areas": [
            {"title": "Statistical Machine Learning & AI", "desc": "Conformal inference, non-convex optimization, neural network theory, and distribution-free uncertainty quantification."},
            {"title": "High-Dimensional Inference", "desc": "Large p small n estimation, sparse covariance estimation, minimax estimation, and random matrix theory."},
            {"title": "Statistical Genetics & Genomics", "desc": "Genome-wide association mapping, single-cell RNA-seq statistical models, and phylogenetic inference."},
            {"title": "Biostatistics & Public Health Data", "desc": "Survival analysis, clinical trial design, causal inference, and epidemiological Bayesian modeling."}
        ],
        "facilities": [
            "Jones Laboratory computational research labs and collaborative spaces",
            "Data Science Institute (DSI) high-throughput computing facilities",
            "Biostatistics and Genomics Core computational clusters"
        ],
        "events": [
            {"title": "Statistics Department Colloquium", "speaker": "Invited Statistical Researchers", "date": "Mondays at 4:00 PM", "loc": "Jones 304"},
            {"title": "Machine Learning & Theory Seminar", "speaker": "Prof. Rina Foygel Barber & Guests", "date": "Wednesdays at 2:00 PM", "loc": "Jones 226"}
        ],
        "contact": {
            "phone": "(773) 702-8333",
            "email": "stats-info@uchicago.asia",
            "office": "Jones Laboratory, Room 222"
        }
    },
    {
        "id": "pritzker-school-of-molecular-engineering",
        "slug": "pritzker-school-of-molecular-engineering",
        "name": "Pritzker School of Molecular Engineering",
        "division": "Pritzker School of Molecular Engineering",
        "division_slug": "pme",
        "building": "William Eckhardt Research Center",
        "address": "5640 S. Ellis Ave, Chicago, IL 60637",
        "chair": "Dean Nadya Mason",
        "tagline": "Engineering from the Molecular Level Up to Solve Global Challenges",
        "hero_image": "../assets/subpage_media/nano-lab-1600-crop.jpg",
        "description": "The Pritzker School of Molecular Engineering (PME) is the first school in the United States dedicated to molecular engineering. Founded in partnership with Argonne National Laboratory, PME integrates physical sciences, life sciences, and engineering to tackle pressing global challenges in quantum information, immunoengineering, sustainable energy, and materials design.",
        "highlights": [
            "First dedicated School of Molecular Engineering in the nation",
            "Headquarters of the Chicago Quantum Exchange and national quantum initiatives",
            "World-leading cleanrooms, cryogenics, and molecular synthesis facilities in the Eckhardt Research Center",
            "Interdisciplinary faculty spanning medicine, physics, chemistry, and computational biology"
        ],
        "undergrad_program": "The B.S. in Molecular Engineering provides an innovative curriculum combining chemistry, physics, biology, and applied mathematics with concentrations in Quantum Engineering, Immunoengineering, and Chemical/Materials Engineering.",
        "masters_program": "Master of Engineering (M.Eng.) programs offering specialized technical and leadership training in quantum engineering, bioengineering, and clean energy.",
        "phd_program": "The Ph.D. in Molecular Engineering offers an interdisciplinary doctoral curriculum where students work across traditional departmental boundaries, supported by full 5-year fellowships, competitive stipends, and research grants.",
        "research_areas": [
            {"title": "Quantum Engineering & Technology", "desc": "Solid-state quantum bits, quantum optics, neutral atom processors, quantum internet, and cryogenic electronics."},
            {"title": "Immunoengineering & Cancer Therapy", "desc": "Antigen-specific immunotherapy, biomaterials for lymphatic drug delivery, engineered vaccines, and cellular therapeutics."},
            {"title": "Materials for Energy & Sustainability", "desc": "Next-generation solid-state batteries, electrocatalysis, self-healing polymers, and water purification membranes."},
            {"title": "Computational & AI Molecular Design", "desc": "Machine learning for molecular discovery, multi-scale simulation, free energy calculations, and de novo peptide design."}
        ],
        "facilities": [
            "Pritzker Nanofabrication Facility (PNF) ISO Class 5 cleanrooms",
            "Soft Matter Characterization and Bioengineering Core",
            "Advanced Battery and Materials Characterization Suite",
            "High-Field Cryogenic Quantum Measurement Laboratory"
        ],
        "events": [
            {"title": "PME Distinguished Colloquium", "speaker": "Dean Nadya Mason & Invited Pioneers", "date": "Wednesdays at 4:00 PM", "loc": "Eckhardt ERC 161"},
            {"title": "Quantum Information & Technology Seminar", "speaker": "Prof. David Awschalom & Guests", "date": "Tuesdays at 11:00 AM", "loc": "ERC 201"}
        ],
        "contact": {
            "phone": "(773) 834-2057",
            "email": "pme-admissions@uchicago.asia",
            "office": "William Eckhardt Research Center, Suite 299"
        }
    },
    {
        "id": "department-of-biochemistry-and-molecular-biology",
        "slug": "department-of-biochemistry-and-molecular-biology",
        "name": "Department of Biochemistry & Molecular Biology",
        "division": "Biological Sciences Division",
        "division_slug": "bsd",
        "building": "Gordon Center for Integrative Science",
        "address": "929 E. 57th St, Chicago, IL 60637",
        "chair": "Prof. Tobin Sosnick",
        "tagline": "Unraveling the Macromolecular Machinery of Life",
        "hero_image": "../assets/subpage_media/petri-dish-sample.jpg",
        "description": "The Department of Biochemistry and Molecular Biology (BMB) investigates the structural, chemical, and physical mechanisms governing biological processes at the molecular scale. From groundbreaking discoveries in RNA epigenetics to macromolecular crystallography and molecular dynamics simulations of membrane proteins, BMB faculty are at the forefront of biochemical discovery.",
        "highlights": [
            "Discovered reversible RNA methylation and founded the field of epitranscriptomics (Prof. Chuan He)",
            "Pioneered theoretical modeling of ion channels and free energy perturbation in membranes (Prof. Benoît Roux)",
            "State-of-the-art Cryo-EM and biophysical characterization infrastructure in the Gordon Center",
            "Interdisciplinary training across chemistry, structural biology, and medicine"
        ],
        "undergrad_program": "The undergraduate curriculum in Biochemistry, offered through the College's Biological Sciences Collegiate Division, prepares students for doctoral research and medical careers with deep laboratory immersion.",
        "masters_program": "Collaborative master's credentials through the Biological Sciences Division.",
        "phd_program": "The Ph.D. in Biochemistry and Molecular Biology provides comprehensive, laboratory-centered training supported by competitive 5-year doctoral fellowships covering full tuition, living stipend, and health benefits.",
        "research_areas": [
            {"title": "RNA Biology & Epitranscriptomics", "desc": "Post-transcriptional RNA modifications, m6A methylation, RNA-protein complexes, and regulatory noncoding RNAs."},
            {"title": "Structural Biology & Cryo-EM", "desc": "Atomic-resolution Cryo-EM structures of membrane channels, ribosomal complexes, and molecular machines."},
            {"title": "Protein Folding & Dynamics", "desc": "Experimental and computational mechanisms of protein folding, misfolding, allostery, and conformational transitions."},
            {"title": "Chemical Biology & Therapeutics", "desc": "Design of chemical probes, synthetic biology tools, targeted protein degradation, and enzyme mechanisms."}
        ],
        "facilities": [
            "Advanced Cryogenic Electron Microscopy (Cryo-EM) Core Facility",
            "Biophysical Core Facility (CD, ITC, Surface Plasmon Resonance, Mass Spec)",
            "Gordon Center for Integrative Science biomolecular synthesis suites"
        ],
        "events": [
            {"title": "Biochemistry Department Seminar Series", "speaker": "Invited Biochemical Scholars", "date": "Wednesdays at 12:00 PM", "loc": "GCIS W301"},
            {"title": "Molecular Biophysics Workshop", "speaker": "Prof. Tobin Sosnick & Faculty", "date": "Fridays at 1:30 PM", "loc": "GCIS W242"}
        ],
        "contact": {
            "phone": "(773) 702-1330",
            "email": "bmb-admissions@uchicago.asia",
            "office": "Gordon Center for Integrative Science, Suite W242"
        }
    },
    {
        "id": "department-of-history",
        "slug": "department-of-history",
        "name": "Department of History",
        "division": "Social Sciences Division",
        "division_slug": "ssd",
        "building": "Social Science Research Building",
        "address": "1126 E. 59th St, Chicago, IL 60637",
        "chair": "Prof. Jane Dailey",
        "tagline": "Global Historical Scholarship, Critical Archival Inquiry, and Field-Defining Thought",
        "hero_image": "../assets/subpage_media/mainquadfall.png",
        "description": "The Department of History at the University of Chicago is internationally celebrated for transformative scholarship spanning global, trans-regional, intellectual, legal, and economic history. Located in the landmark Social Science Research Building, our faculty have fundamentally reshaped modern historical understanding, from postcolonial historiography to the 'Great Divergence' in global capitalism.",
        "highlights": [
            "Home to leading global historians including Kenneth Pomeranz, Dipesh Chakrabarty, and Tara Zahra",
            "Birthplace of foundational methodologies in archival research, transnational history, and intellectual history",
            "Vibrant doctoral community with global research archives access across Asia, Europe, Africa, and the Americas",
            "Rich interdisciplinary ties to the Chicago Center for Contemporary Theory and the Pozen Family Center for Human Rights"
        ],
        "undergrad_program": "The B.A. in History empowers students to interrogate primary source evidence, master historiographical argumentation, and complete an ambitious, original Bachelor's thesis under faculty mentorship.",
        "masters_program": "Master of Arts in Social Sciences (MAPSS) with History specialization.",
        "phd_program": "The Ph.D. in History is one of the premier doctoral programs in the world, preparing students for scholarly careers with complete funding packages covering tuition, competitive stipends, and international archival travel grants.",
        "research_areas": [
            {"title": "Global, Transnational & Imperial History", "desc": "Comparative development, colonial empires, migration, and the political economy of globalization."},
            {"title": "East Asian History & The Great Divergence", "desc": "Early modern and modern China, Japan, environmental history, and comparative state formation."},
            {"title": "American Political & Legal History", "desc": "Reconstruction, civil rights, constitutional jurisprudence, labor history, and presidential power."},
            {"title": "Intellectual History & Radical Ideas", "desc": "Renaissance humanism, Enlightenment philosophy, postcolonial thought, and historiographical methodology."}
        ],
        "facilities": [
            "Social Science Research Building historic seminar halls and archives",
            "The University of Chicago Joseph Regenstein Library Special Collections Research Center",
            "Center for East Asian Studies and Nicholson Center for British Studies"
        ],
        "events": [
            {"title": "History Department Colloquium", "speaker": "Faculty & Visiting International Scholars", "date": "Tuesdays at 4:30 PM", "loc": "SSRB 224"},
            {"title": "Global & Transnational History Workshop", "speaker": "Prof. Kenneth Pomeranz & Guests", "date": "Thursdays at 5:00 PM", "loc": "SSRB 106"}
        ],
        "contact": {
            "phone": "(773) 702-8397",
            "email": "history-dept@uchicago.asia",
            "office": "Social Science Research Building, Room 224"
        }
    },
    {
        "id": "department-of-philosophy",
        "slug": "department-of-philosophy",
        "name": "Department of Philosophy",
        "division": "Humanities Division",
        "division_slug": "humanities",
        "building": "Stuart Hall",
        "address": "5835 S. Greenwood Ave, Chicago, IL 60637",
        "chair": "Prof. Matthew Boyle",
        "tagline": "Rigorous Conceptual Inquiry into Mind, Language, Ethics, and the History of Thought",
        "hero_image": "../assets/subpage_media/flower-bed-recrop.jpg",
        "description": "The Department of Philosophy at the University of Chicago is celebrated for its distinctive integration of historical depth and rigorous systematic philosophy. Our scholars lead the world in ancient Greek philosophy, German idealism, philosophy of mind and action, ordinary language philosophy, and contemporary ethics and political philosophy.",
        "highlights": [
            "Renowned faculty including Martha C. Nussbaum, Jonathan Lear, Agnes Callard, and James Conant",
            "Global center for Kant, German Idealism, and the Wittgensteinian tradition",
            "Close collaboration with the Law School, Department of Classics, and Committee on Social Thought",
            "Vibrant undergraduate philosophic debate societies and doctoral mentorship"
        ],
        "undergrad_program": "The B.A. in Philosophy offers intensive training in critical reasoning, textual analysis, and philosophical argumentation, covering history of philosophy, logic, ethics, and metaphysics.",
        "masters_program": "Interdisciplinary master's credentials through the Humanities Division.",
        "phd_program": "The Ph.D. in Philosophy is a world-class doctoral program preparing researchers and teachers of philosophy, supported by comprehensive multi-year fellowships.",
        "research_areas": [
            {"title": "History of Philosophy (Ancient & Modern)", "desc": "Plato, Aristotle, Hellenistic philosophy, Kant, Hegel, and 19th-century European philosophy."},
            {"title": "Philosophy of Mind & Action", "desc": "Nature of agency, intentionality, self-consciousness, practical reason, and philosophical psychology."},
            {"title": "Ethics, Political Philosophy & Law", "desc": "Capabilities approach, theories of justice, moral emotions, democratic theory, and constitutional jurisprudence."},
            {"title": "Philosophy of Language & Logic", "desc": "Wittgenstein, ordinary language philosophy, truth theories, skepticism, and formal semantics."}
        ],
        "facilities": [
            "Stuart Hall philosophical lecture rooms and departmental library",
            "Center for Law, Philosophy, and Human Values (Law School)",
            "Franke Institute for the Humanities seminar spaces"
        ],
        "events": [
            {"title": "Philosophy Department Colloquium", "speaker": "Distinguished Visiting Philosophers", "date": "Fridays at 3:30 PM", "loc": "Stuart Hall 104"},
            {"title": "Practical Philosophy Workshop", "speaker": "Prof. Martha Nussbaum & Prof. Matthew Boyle", "date": "Mondays at 4:30 PM", "loc": "Stuart Hall 209"}
        ],
        "contact": {
            "phone": "(773) 702-8513",
            "email": "philosophy-dept@uchicago.asia",
            "office": "Stuart Hall, Room 202"
        }
    },
    {
        "id": "department-of-political-science",
        "slug": "department-of-political-science",
        "name": "Department of Political Science",
        "division": "Social Sciences Division",
        "division_slug": "ssd",
        "building": "Pick Hall for International Studies",
        "address": "5828 S. University Ave, Chicago, IL 60637",
        "chair": "Prof. Susan Stokes",
        "tagline": "Theoretical Rigor, Empirical Power, and Field-Defining International Scholarship",
        "hero_image": "../assets/subpage_media/mainquadfall.png",
        "description": "The Department of Political Science at the University of Chicago is one of the most distinguished centers of political scholarship in the world. Known for fostering groundbreaking approaches in international relations realism, democratic accountability, political theory, and racial politics, our faculty address the foundational questions of power, governance, and human society.",
        "highlights": [
            "Home to leading political theorists and international relations realists including John Mearsheimer and Robert Pape",
            "Pioneered the Chicago Center on Democracy and the Chicago Project on Security and Threats (CPOST)",
            "Deep integration across quantitative empirical methods, formal political economy, and political philosophy",
            "Outstanding placement record for doctoral graduates in top academic and policy institutions worldwide"
        ],
        "undergrad_program": "The B.A. in Political Science gives students mastery over international relations, political theory, American politics, and comparative politics, culminating in rigorous senior research.",
        "masters_program": "Master of Arts in International Relations (CIR) — the nation's oldest graduate program in international affairs.",
        "phd_program": "The Ph.D. in Political Science trains visionary scholars with multi-year comprehensive fellowships covering tuition, stipend, and fieldwork funding.",
        "research_areas": [
            {"title": "International Relations & Grand Strategy", "desc": "Offensive realism, great power competition, nuclear deterrence, international security, and war dynamics."},
            {"title": "Comparative Politics & Democratization", "desc": "Democratic backsliding, clientelism, authoritarian regimes, political institutions, and electoral accountability."},
            {"title": "Political Theory", "desc": "Democratic theory, republicanism, feminist political theory, historical political philosophy, and critical theory."},
            {"title": "American Politics & Political Behavior", "desc": "Racial politics, public opinion, congressional behavior, party polarization, and voting rights."}
        ],
        "facilities": [
            "Pick Hall for International Studies research suites and seminar halls",
            "Chicago Center on Democracy",
            "Chicago Project on Security and Threats (CPOST)"
        ],
        "events": [
            {"title": "Program on International Security Policy (PISP)", "speaker": "Prof. John Mearsheimer & Guests", "date": "Tuesdays at 12:15 PM", "loc": "Pick Hall 506"},
            {"title": "Political Theory Workshop", "speaker": "Invited Theorists and Faculty", "date": "Mondays at 4:30 PM", "loc": "Pick Hall 218"}
        ],
        "contact": {
            "phone": "(773) 702-8050",
            "email": "polisci-dept@uchicago.asia",
            "office": "Pick Hall, Room 418"
        }
    },
    {
        "id": "department-of-sociology",
        "slug": "department-of-sociology",
        "name": "Department of Sociology",
        "division": "Social Sciences Division",
        "division_slug": "ssd",
        "building": "Social Science Research Building",
        "address": "1126 E. 59th St, Chicago, IL 60637",
        "chair": "Prof. Jenny Trinitapoli",
        "tagline": "The Founding Department of American Sociology: Urban, Computational, and Structural Insights",
        "hero_image": "../assets/subpage_media/mainquadfall.png",
        "description": "Founded in 1892 as the first department of sociology in the United States, the UChicago Department of Sociology established the discipline itself. The 'Chicago School of Sociology' pioneered modern urban ethnography, quantitative social network analysis, computational sociology, and demographic modeling.",
        "highlights": [
            "First department of sociology founded in the United States (1892)",
            "Home to the American Journal of Sociology (AJS), the premier journal in the field",
            "Pioneered urban ethnography, social ecology, and modern computational sociological analysis (Knowledge Lab)",
            "Comprehensive doctoral training with full fellowship support"
        ],
        "undergrad_program": "The B.A. in Sociology provides analytical and empirical training to decode urban processes, stratification, social networks, and cultural institutions.",
        "masters_program": "Collaborative master's credentials through the Division of the Social Sciences (MAPSS).",
        "phd_program": "The Ph.D. in Sociology prepares preeminent researchers through intensive training in qualitative and quantitative methods, supported by 5-year full funding awards.",
        "research_areas": [
            {"title": "Urban Sociology & Ethnography", "desc": "Spatial segregation, community dynamics, neighborhood inequality, and urban development."},
            {"title": "Computational Sociology & Science Studies", "desc": "Large-scale text mining, network diffusion, citation graphs, and discovery acceleration (Knowledge Lab)."},
            {"title": "Sociological Theory & Organizations", "desc": "Social process theory, institutionalism, professionalization, and history of sociology."},
            {"title": "Demography & Health Inequality", "desc": "Population studies, reproductive health, global disease vulnerability, and life course transitions."}
        ],
        "facilities": [
            "Social Science Research Building sociology seminar commons",
            "Knowledge Lab computational facilities and big data infrastructure",
            "Population Research Center (PRC) demographic computing facilities"
        ],
        "events": [
            {"title": "Sociology Department Colloquium", "speaker": "Visiting Sociological Scholars", "date": "Thursdays at 3:30 PM", "loc": "SSRB 106"},
            {"title": "Urban Sociology Workshop", "speaker": "Faculty & Doctoral Researchers", "date": "Mondays at 12:00 PM", "loc": "SSRB 224"}
        ],
        "contact": {
            "phone": "(773) 702-8686",
            "email": "sociology-info@uchicago.asia",
            "office": "Social Science Research Building, Room 307"
        }
    },
    {
        "id": "department-of-english",
        "slug": "department-of-english",
        "name": "Department of English Language & Literature",
        "division": "Humanities Division",
        "division_slug": "humanities",
        "building": "Walker Museum Building",
        "address": "1115 E. 58th St, Chicago, IL 60637",
        "chair": "Prof. Deborah L. Nelson",
        "tagline": "Critical Rigor, Literary Imagination, and Aesthetic Interpretation",
        "hero_image": "../assets/subpage_media/flower-bed-recrop.jpg",
        "description": "The Department of English Language and Literature at the University of Chicago is renowned for visionary scholarship in literary history, critical theory, cultural studies, and creative writing. Our faculty pioneer influential approaches in affect theory, media aesthetics, early modern drama, American literature, and postcolonial poetics.",
        "highlights": [
            "Home to Guggenheim Fellows, Pulitzer Prize winners, and leading literary theorists",
            "Pioneered critical affect theory and visual culture studies (Critical Inquiry journal)",
            "Rich ties to the Chicago Review and the Committee on Creative Writing",
            "Renowned doctoral program with comprehensive funding and international archive access"
        ],
        "undergrad_program": "The B.A. in English provides deep textual analysis, historical interpretation, and creative expression, offering courses from medieval romance to contemporary global fiction.",
        "masters_program": "Master of Arts Program in the Humanities (MAPH) with English concentration.",
        "phd_program": "The Ph.D. in English trains scholars and teachers of literature, supported by 5-year full fellowship packages covering tuition, stipend, and research allowances.",
        "research_areas": [
            {"title": "Critical Theory & Cultural Studies", "desc": "Aesthetic theory, affect theory, political criticism, and cultural studies."},
            {"title": "Early Modern & Renaissance Literature", "desc": "Shakespeare, early modern drama, poetry, religious culture, and print history."},
            {"title": "American Literature & Modernism", "desc": "19th- and 20th-century American fiction, African American literature, poetics, and Cold War culture."},
            {"title": "Media Aesthetics & Visual Culture", "desc": "Word-and-image relations, cinematic adaptation, digital humanities, and publication history."}
        ],
        "facilities": [
            "Walker Museum Building departmental seminars and student reading rooms",
            "Critical Inquiry editorial suites",
            "Special Collections Research Center at Regenstein Library"
        ],
        "events": [
            {"title": "English Department Faculty Colloquium", "speaker": "Prof. Deborah Nelson & Faculty", "date": "Thursdays at 4:30 PM", "loc": "Walker 201"},
            {"title": "Poetry & Poetics Workshop", "speaker": "Visiting Poets and Scholars", "date": "Tuesdays at 5:00 PM", "loc": "Walker 103"}
        ],
        "contact": {
            "phone": "(773) 702-8536",
            "email": "english-dept@uchicago.asia",
            "office": "Walker Museum Building, Room 202"
        }
    },
    {
        "id": "chicago-booth-school-of-business",
        "slug": "chicago-booth-school-of-business",
        "name": "Chicago Booth School of Business",
        "division": "Professional Schools",
        "division_slug": "professional",
        "building": "Charles M. Harper Center",
        "address": "5807 S. Woodlawn Ave, Chicago, IL 60637",
        "chair": "Dean Madhav Rajan",
        "tagline": "Empowering Leaders with The Chicago Approach to Business Education",
        "hero_image": "../assets/subpage_media/mainquadfall.png",
        "description": "Founded in 1898, the University of Chicago Booth School of Business is the second-oldest business school in the world and the proud home of 10 Nobel laureates in Economic Sciences. Known worldwide for 'The Chicago Approach'—a rigorous, discipline-based education grounded in fundamental principles of economics, statistics, and behavioral science—Chicago Booth shapes the global business landscape.",
        "highlights": [
            "10 Nobel Laureates in Economic Sciences affiliated with Chicago Booth faculty",
            "Consistently ranked among the top MBA programs in the world",
            "Historic Charles M. Harper Center designed by world-renowned architect Rafael Viñoly",
            "Global campuses in Chicago (Hyde Park and Downtown), London, and Hong Kong"
        ],
        "undergrad_program": "The Trott Business Program and the Booth Undergraduate Business Studies curriculum offer College students rigorous foundational coursework in finance, accounting, and marketing.",
        "masters_program": "Full-Time MBA, Evening MBA, Weekend MBA, and Executive MBA (XP) programs delivering transformative leadership development.",
        "phd_program": "The Ph.D. in Business is the first doctoral business program founded in the United States, offering specialized tracks in Finance, Accounting, Economics, Marketing, and Behavioral Science with full financial support.",
        "research_areas": [
            {"title": "Finance & Efficient Capital Markets", "desc": "Asset pricing, corporate finance, financial derivatives, banking fragility, and empirical investment research."},
            {"title": "Behavioral Science & Decision Research", "desc": "Behavioral economics, decision heuristics, choice architecture (Nudge), and consumer psychology."},
            {"title": "Accounting & Corporate Governance", "desc": "Financial statement analysis, auditing standards, executive compensation, and disclosure economics."},
            {"title": "Entrepreneurship & Social Innovation", "desc": "Venture capital, startup acceleration, private equity, and impact investing (Polsky Center and Rustandy Center)."}
        ],
        "facilities": [
            "Charles M. Harper Center state-of-the-art tiered auditoriums and trading simulation labs",
            "Polsky Center for Entrepreneurship and Innovation",
            "Rustandy Center for Social Sector Innovation",
            "Fama-Miller Center for Research in Finance"
        ],
        "events": [
            {"title": "Booth Finance Seminar", "speaker": "Prof. Eugene Fama & Prof. Douglas Diamond", "date": "Tuesdays at 1:30 PM", "loc": "Harper Center 104"},
            {"title": "Behavioral Science & Decision Research Colloquium", "speaker": "Prof. Richard Thaler & Guests", "date": "Wednesdays at 3:00 PM", "loc": "Harper Center 340"}
        ],
        "contact": {
            "phone": "(773) 702-7369",
            "email": "booth-admissions@uchicago.asia",
            "office": "Charles M. Harper Center, Suite 100"
        }
    },
    {
        "id": "university-of-chicago-law-school",
        "slug": "university-of-chicago-law-school",
        "name": "The University of Chicago Law School",
        "division": "Professional Schools",
        "division_slug": "professional",
        "building": "The Law School Complex",
        "address": "1111 E. 60th St, Chicago, IL 60637",
        "chair": "Dean Thomas J. Miles",
        "tagline": "The Premier Law School for Socratic Inquiry and Law & Economics",
        "hero_image": "../assets/subpage_media/mainquadfall.png",
        "description": "The University of Chicago Law School offers a rigorous, interdisciplinary legal education characterized by unyielding commitment to free inquiry, the Socratic method, and empirical scholarship. As the birthplace of Law and Economics, Chicago Law trains visionary attorneys, judges, legal scholars, and public servants.",
        "highlights": [
            "Consistently ranked among the top 3 law schools in the nation",
            "Birthplace and global capital of the Law and Economics movement",
            "Historic landmark Eero Saarinen-designed Law School building",
            "Nationally renowned faculty in Constitutional Law, Jurisprudence, First Amendment, and Antitrust"
        ],
        "undergrad_program": "The Law, Letters, and Society major in the College offers undergraduates interdisciplinary training in legal institutions and political philosophy.",
        "masters_program": "Master of Laws (LL.M.) for international attorneys and Master of Legal Studies (MLS) for non-lawyer professionals.",
        "phd_program": "Doctor of Juridical Science (J.S.D.) for scholars preparing for careers in legal academia.",
        "research_areas": [
            {"title": "Law & Economics", "desc": "Economic analysis of legal rules, antitrust law, corporate governance, bankruptcy, and regulation."},
            {"title": "Constitutional Law & Free Expression", "desc": "First Amendment jurisprudence, originalism, separation of powers, and the Free Speech Century."},
            {"title": "Jurisprudence & Legal Philosophy", "desc": "Philosophical foundations of law, the capabilities approach, justice theories, and legal realism."},
            {"title": "Criminal Justice & Empirical Legal Studies", "desc": "Sentencing reform, judicial behavior, criminal procedure, and data-driven legal analytics."}
        ],
        "facilities": [
            "D'Angelo Law Library research facilities",
            "Mandel Legal Aid Clinic client service suites",
            "Coase-Sandor Institute for Law and Economics",
            "Weymouth Kirkland Courtroom"
        ],
        "events": [
            {"title": "Fulton Lecture in Legal Scholarship", "speaker": "Dean Thomas J. Miles & Guest Jurists", "date": "Thursdays at 12:15 PM", "loc": "Kirkland Courtroom"},
            {"title": "Constitutional Law Roundtable", "speaker": "Prof. Geoffrey Stone & Prof. William Baude", "date": "Mondays at 4:00 PM", "loc": "Law School Room V"}
        ],
        "contact": {
            "phone": "(773) 702-9484",
            "email": "law-admissions@uchicago.asia",
            "office": "The Law School, 1111 E. 60th St"
        }
    },
    {
        "id": "harris-school-of-public-policy",
        "slug": "harris-school-of-public-policy",
        "name": "Harris School of Public Policy",
        "division": "Professional Schools",
        "division_slug": "professional",
        "building": "The Keller Center",
        "address": "1307 E. 60th St, Chicago, IL 60637",
        "chair": "Dean Ethan Bueno de Mesquita",
        "tagline": "Evidence-Based Policy: Data, Economics, and Real-World Impact",
        "hero_image": "../assets/subpage_media/harris-students-networking.jpg",
        "description": "The Harris School of Public Policy at the University of Chicago approaches policymaking through the lens of data science and microeconomic analysis. Housed in the LEED Platinum Keller Center, Harris faculty and students tackle global climate policy, urban education, crime reduction, municipal finance, and international governance.",
        "highlights": [
            "LEED Platinum Keller Center designed by Farr Associates and Studio Gang",
            "Home to Nobel Laureate in Economic Sciences Prof. James A. Robinson (2024)",
            "World-renowned Urban Labs: Crime Lab, Education Lab, Health Lab, Poverty Lab",
            "Pioneering degrees in Computational Analysis and Public Policy (MSCAPP)"
        ],
        "undergrad_program": "The Public Policy Studies major in the College gives undergraduates rigorous training in policy design, econometrics, and program evaluation.",
        "masters_program": "Master of Public Policy (MPP), MS in Computational Analysis and Public Policy (MSCAPP), and Evening Master's credentials.",
        "phd_program": "The Ph.D. in Public Policy trains researchers in quantitative policy evaluation, political economy, and applied microeconomics with complete 5-year fellowship funding.",
        "research_areas": [
            {"title": "Urban Policy & Crime Mitigation", "desc": "Evidence-based violence intervention, police reform, urban schooling, and youth development (Urban Labs)."},
            {"title": "Political Economy & Governance", "desc": "Institutional development, authoritarian politics, conflict studies, and voting behavior."},
            {"title": "Energy & Environmental Policy", "desc": "Carbon pricing, global climate negotiations, energy access in developing nations, and renewable transitions."},
            {"title": "Child Development & Education Policy", "desc": "Early childhood interventions, parental investments, school choice mechanisms, and social mobility."}
        ],
        "facilities": [
            "The Keller Center Forum and collaborative policy design suites",
            "University of Chicago Urban Labs research command center",
            "Energy Policy Institute at Chicago (EPIC)",
            "Center for Municipal Finance research laboratories"
        ],
        "events": [
            {"title": "Harris Policy Forum & Dean's Lecture", "speaker": "Dean Ethan Bueno de Mesquita", "date": "Tuesdays at 12:00 PM", "loc": "Keller Center Forum"},
            {"title": "Political Economy & Development Seminar", "speaker": "Prof. James A. Robinson & Guests", "date": "Thursdays at 3:30 PM", "loc": "Keller 1022"}
        ],
        "contact": {
            "phone": "(773) 702-8400",
            "email": "harris-admissions@uchicago.asia",
            "office": "The Keller Center, 1307 E. 60th St"
        }
    },
    {
        "id": "pritzker-school-of-medicine",
        "slug": "pritzker-school-of-medicine",
        "name": "Pritzker School of Medicine",
        "division": "Biological Sciences Division",
        "division_slug": "bsd",
        "building": "Biological Sciences Learning Center",
        "address": "924 E. 57th St, Chicago, IL 60637",
        "chair": "Dean Vineet Arora / Dr. Mark Anderson",
        "tagline": "Translational Medicine, Clinical Excellence, and Compassionate Care",
        "hero_image": "../assets/subpage_media/immunotherapy-researcher.jpg",
        "description": "The Pritzker School of Medicine is one of the top medical schools in the nation, uniquely co-located with the University of Chicago Medical Center and the undergraduate College on a contiguous campus. Pritzker integrates rigorous biomedical science, clinical inquiry, and health equity leadership.",
        "highlights": [
            "Top-ranked medical school embedded within the University of Chicago Medicine health system",
            "Pioneered surgical innovations, bone marrow transplantation, and cancer chemotherapy",
            "Exceptional Medical Scientist Training Program (MSTP / MD-PhD) supported by the NIH",
            "Ranked #1 for student satisfaction and clinical research immersion"
        ],
        "undergrad_program": "Pre-med advising, clinical shadow programs, and research mentorship for undergraduate students in the College.",
        "masters_program": "Master of Science in Public Health Sciences and MS in Biomedical Informatics.",
        "phd_program": "The Medical Scientist Training Program (M.D./Ph.D.) provides integrated clinical and basic science doctoral training with full tuition, stipend, and research allowances.",
        "research_areas": [
            {"title": "Cancer Genetics & Immunotherapy", "desc": "BRCA mutations, cellular therapies, tumor microenvironment targeting, and personalized oncology."},
            {"title": "Cardiovascular Science & Arrhythmias", "desc": "Molecular mechanisms of heart failure, cardiac electrophysiology, and ischemic injury prevention."},
            {"title": "Gastroenterology & Microbiome", "desc": "Inflammatory bowel disease, microbiome-host interactions, and metabolic syndromes."},
            {"title": "Health Equity & Healthcare Quality", "desc": "Physician communication, medical education reform, systemic disparities in health access, and hospital operations."}
        ],
        "facilities": [
            "Center for Care and Discovery (CCD) inpatient clinical pavilions",
            "Biological Sciences Learning Center (BSLC) simulation centers",
            "Comprehensive Cancer Center state-of-the-art research laboratories",
            "Duchossois Family Institute for Microbiome Research"
        ],
        "events": [
            {"title": "Grand Rounds in Medicine", "speaker": "Distinguished Physician-Scientists", "date": "Tuesdays at 8:00 AM", "loc": "BSLC Auditorium"},
            {"title": "Clinical Research & Translational Seminar", "speaker": "Dean Vineet Arora & Faculty", "date": "Thursdays at 12:00 PM", "loc": "CCD Amphitheater"}
        ],
        "contact": {
            "phone": "(773) 702-1939",
            "email": "pritzker-admissions@uchicago.asia",
            "office": "Biological Sciences Learning Center, Room 104"
        }
    },
    {
        "id": "department-of-chemistry",
        "slug": "department-of-chemistry",
        "name": "Department of Chemistry",
        "division": "Physical Sciences Division",
        "division_slug": "psd",
        "building": "Searle Chemistry Laboratory",
        "address": "5735 S. Ellis Ave, Chicago, IL 60637",
        "chair": "Prof. Viresh Rawal",
        "tagline": "Transformative Discoveries Across Synthetic, Biological, Physical, and Theoretical Chemistry",
        "hero_image": "../assets/subpage_media/nano-lab-1600-crop.jpg",
        "description": "Founded in 1892 as one of the inaugural departments of the University of Chicago, the Department of Chemistry has pioneered fundamental discoveries that define modern chemical science, including radiocarbon dating, electron transfer theory, and RNA epigenetics. Home to 15 Nobel laureates and historic Searle Laboratories.",
        "highlights": [
            "15 Nobel Laureates in Chemistry affiliated with the department",
            "Historic Searle Chemistry Laboratory and Kent Chemical Laboratory in Hyde Park",
            "Pioneers in epitranscriptomics, bioconjugation, quantum dynamics, and inorganic nanomaterials",
            "Doctoral program with complete multi-year tuition grants and living stipends"
        ],
        "undergrad_program": "The B.S. and B.A. in Chemistry curriculum combines rigorous foundational lectures in organic, inorganic, physical, and analytical chemistry with extensive research laboratory experience.",
        "masters_program": "Collaborative MS credentials and joint Physical Sciences Division degree programs.",
        "phd_program": "The Ph.D. in Chemistry develops independent doctoral scholars across synthetic organic, chemical biology, inorganic materials, and theoretical chemistry with full 5-year financial support.",
        "research_areas": [
            {"title": "Chemical Biology & Epigenetics", "desc": "Reversible RNA methylation (m6A), targeted covalent modification, cellular imaging probes, and directed evolution."},
            {"title": "Inorganic & Materials Chemistry", "desc": "Colloidal semiconductor nanocrystals, molecular quantum bits, coordination networks, and electrocatalytic materials."},
            {"title": "Physical & Ultrafast Chemistry", "desc": "2D electronic spectroscopy, single-molecule biophysics, femtosecond laser dynamics, and energy transfer."},
            {"title": "Theoretical & Computational Chemistry", "desc": "Electronic structure theory, multiscale molecular dynamics, quantum mechanics/molecular mechanics (QM/MM), and density functional development."}
        ],
        "facilities": [
            "Searle Chemistry Laboratory modern synthetic and analytical suites",
            "Nuclear Magnetic Resonance (NMR) Facility (500-800 MHz spectrometers)",
            "Mass Spectrometry & Proteomics Core",
            "X-Ray Crystallography Diffraction Facility"
        ],
        "events": [
            {"title": "Department of Chemistry Colloquium", "speaker": "Prof. Viresh Rawal & Visiting Scholars", "date": "Mondays at 4:00 PM", "loc": "Kent 107"},
            {"title": "Chemical Biology & Biophysics Seminar", "speaker": "Prof. Chuan He & Faculty", "date": "Thursdays at 1:30 PM", "loc": "Searle 340"}
        ],
        "contact": {
            "phone": "(773) 702-7250",
            "email": "chem-admissions@uchicago.asia",
            "office": "Searle Chemistry Laboratory, Room 304"
        }
    }
]
