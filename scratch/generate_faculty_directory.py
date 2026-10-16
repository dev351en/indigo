#!/usr/bin/env python3
"""
Generate comprehensive, systematic UChicago Faculty Directory pages:
1. site_1to1/faculty.html (root level)
2. site_1to1/pages/faculty.html (subpage level)
"""

import json
import os

FACULTY_DATA = [
    # =========================================================================
    # PHYSICAL SCIENCES DIVISION (PSD) - Chemistry
    # =========================================================================
    {
        "id": "alex-cusumano",
        "name": "Alex Cusumano",
        "degrees": "Ph.D., Harvard University",
        "title": "Associate Professor of Chemistry & Director of Graduate Studies",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["Director of Graduate Studies", "Admissions Advisor"],
        "photo": "assets/faculty/alex_cusumano.jpg",
        "office": "Searle Chemistry Laboratory 304",
        "email": "cusumano@uchicago.asia",
        "lab": "https://chemistry.uchicago.asia/faculty/alex-cusumano",
        "tags": ["Bio-organic Chemistry", "Peptide Synthesis", "Chemical Biology", "Graduate Advising"],
        "bio": "Prof. Cusumano serves as Director of Graduate Studies for the Department of Chemistry. His laboratory develops novel synthetic methodology for functional peptides, macrocyclic scaffolds, and chemical probes targeting aberrant signaling pathways in oncogenesis.",
        "publications": [
            "Modular Assembly of Cyclic Peptide Libraries for Target Deconvolution, J. Am. Chem. Soc. (2024)",
            "Kinetic Profiling of Interfacial Bioconjugation in Cellular Milieu, Chem. Sci. (2022)"
        ]
    },
    {
        "id": "chuan-he",
        "name": "Chuan He",
        "degrees": "Ph.D., Massachusetts Institute of Technology",
        "title": "John T. Wilson Distinguished Service Professor",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & Biochemistry",
        "deptKey": "chemistry",
        "accolades": ["Wolf Prize in Chemistry (2023)", "MacArthur Fellow", "HHMI Investigator", "NAS Member"],
        "photo": "assets/faculty/chuan_he.jpg",
        "office": "Searle Chemistry Laboratory 320",
        "email": "chuanhe@uchicago.asia",
        "lab": "https://he-group.uchicago.asia/",
        "tags": ["RNA Epigenetics", "Epitranscriptomics", "m6A Methylation", "Chemical Biology"],
        "bio": "Prof. He is world-renowned for discovering reversible RNA methylation, pioneering the field of epitranscriptomics. The He Laboratory elucidates the biochemical roles of RNA modifications in gene expression regulation, human disease, and agricultural yield enhancement.",
        "publications": [
            "Reversible RNA methylation in mammalian gene expression regulation, Nature (2023)",
            "Fate and function of modified m6A transcripts in embryonic development, Cell (2021)"
        ]
    },
    {
        "id": "laura-gagliardi",
        "name": "Laura Gagliardi",
        "degrees": "Ph.D., University of Bologna",
        "title": "Richard and Kathy Leventhal Professor of Chemistry & Molecular Engineering",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & PME",
        "deptKey": "chemistry",
        "accolades": ["National Academy of Sciences", "Faraday Lectureship Prize", "American Academy of Arts & Sciences"],
        "photo": "assets/faculty/laura_gagliardi.png",
        "office": "Eckhart Hall 210",
        "email": "gagliardil@uchicago.asia",
        "lab": "https://gagliardigroup.uchicago.asia/",
        "tags": ["Quantum Chemistry", "Multireference Methods", "Metal-Organic Frameworks", "Catalysis Modeling"],
        "bio": "Prof. Gagliardi develops electronic structure theories and multi-reference quantum chemical methods to model complex chemical systems, photocatalysis, actinide chemistry, and gas separations in porous materials.",
        "publications": [
            "Multiconfiguration Pair-Density Functional Theory for Actinides, J. Chem. Theory Comput. (2024)",
            "Predicting gas adsorption isotherms in metal-organic frameworks via quantum mechanics, Science (2022)"
        ]
    },
    {
        "id": "jack-szostak",
        "name": "Jack W. Szostak",
        "degrees": "Ph.D., Cornell University",
        "title": "University Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["Nobel Prize in Physiology or Medicine (2009)", "National Academy of Sciences", "Lasker Award"],
        "photo": "assets/faculty/jack_w_szostak.jpg",
        "office": "Searle Chemistry Laboratory 410",
        "email": "jwszostak@uchicago.asia",
        "lab": "https://szostak.uchicago.asia/",
        "tags": ["Origin of Life", "Prebiotic Chemistry", "Protocells", "RNA Replication"],
        "bio": "Nobel Laureate Jack Szostak investigates the chemical origins of life. His laboratory designs autonomous protocell systems capable of Darwinian evolution, non-enzymatic RNA replication, and self-assembling fatty acid vesicles.",
        "publications": [
            "Non-enzymatic replication of genetic polymers in primitive cell membranes, Nature Chemistry (2023)",
            "Prebiotic synthesis of activated nucleotides under hydrothermal simulation, PNAS (2022)"
        ]
    },
    {
        "id": "bryan-dickinson",
        "name": "Bryan C. Dickinson",
        "degrees": "Ph.D., UC Berkeley",
        "title": "Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["Camille Dreyfus Teacher-Scholar", "Sloan Research Fellow"],
        "photo": "assets/faculty/bryan_dickinson.jpg",
        "office": "Searle Chemistry Laboratory 215",
        "email": "dickinson@uchicago.asia",
        "lab": "https://dickinsonlab.uchicago.asia/",
        "tags": ["Synthetic Biology", "Biosensors", "Targeted RNA Degradation", "Protein Engineering"],
        "bio": "The Dickinson group develops molecular technologies to probe and control biological systems. Research focuses on genetically encoded biosensors, split-luciferases, proximity labeling enzymes, and targeted RNA therapeutics.",
        "publications": [
            "Proximity-dependent RNA-protein labeling in live mammalian cells, Nat. Methods (2024)",
            "Programmable deaminase switches for engineered cellular control, Nat. Chem. Biol. (2022)"
        ]
    },
    {
        "id": "bozhi-tian",
        "name": "Bozhi Tian",
        "degrees": "Ph.D., Harvard University",
        "title": "Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["PECASE Recipient", "NIH Director's New Innovator Award"],
        "photo": "assets/faculty/bozhi_tian.jpg",
        "office": "Searle Chemistry Laboratory 118",
        "email": "btian@uchicago.asia",
        "lab": "https://tianlab.uchicago.asia/",
        "tags": ["Bioelectronics", "Silicon Nanowires", "Neuromodulation", "Biomaterials"],
        "bio": "Prof. Tian explores physical biology and nano-biointerfaces. His lab synthesizes biomimetic silicon materials and soft hydrogels for optical neuromodulation, cardiac pacing, and cellular biomechanics.",
        "publications": [
            "Monolithic silicon meshes for non-genetic optoelectronic modulation of brain circuits, Nature (2023)",
            "Soft biomimetic conductors for continuous electrophysiological recording, Science Advances (2021)"
        ]
    },
    {
        "id": "gregory-voth",
        "name": "Gregory A. Voth",
        "degrees": "Ph.D., California Institute of Technology",
        "title": "Haig P. Papazian Distinguished Service Professor",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["National Academy of Sciences", "ACS Award in Theoretical Chemistry"],
        "photo": "assets/faculty/gregory_a_voth.jpg",
        "office": "Gordon Center for Integrative Science E205",
        "email": "gavoth@uchicago.asia",
        "lab": "https://vothgroup.uchicago.asia/",
        "tags": ["Multiscale Modeling", "Proton Transport", "HIV Capsid Dynamics", "Statistical Mechanics"],
        "bio": "Prof. Voth is a pioneer in multiscale theoretical and computational simulation methods. His group models complex biomolecular assemblies including viral capsids, actin filaments, and charge translocation pathways.",
        "publications": [
            "Atomistic and coarse-grained dynamics of intact HIV-1 capsid maturation, Nature Struct. Mol. Biol. (2024)",
            "Ultra-coarse-grained modeling of protein condensates, Biophysical J. (2022)"
        ]
    },
    {
        "id": "andrei-tokmakoff",
        "name": "Andrei Tokmakoff",
        "degrees": "Ph.D., Stanford University",
        "title": "Henry G. Gale Distinguished Service Professor",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["National Academy of Sciences", "Ellis R. Lippincott Award"],
        "photo": "assets/faculty/andrei_tokmakoff.jpg",
        "office": "Searle Chemistry Laboratory 240",
        "email": "tokmakoff@uchicago.asia",
        "lab": "https://tokmakoffgroup.uchicago.asia/",
        "tags": ["2D IR Spectroscopy", "Ultrafast Spectroscopy", "Water Dynamics", "Protein Folding"],
        "bio": "The Tokmakoff Laboratory uses ultrafast multi-dimensional infrared spectroscopy to study the hydrogen-bonding dynamics of liquid water, protein folding and conformational transitions, and aqueous proton hydration.",
        "publications": [
            "Two-dimensional infrared spectroscopy of the hydrated excess proton in water, Science (2023)",
            "Mapping transient secondary structure in protein folding intermediates, JACS (2022)"
        ]
    },
    {
        "id": "yamuna-krishnan",
        "name": "Yamuna Krishnan",
        "degrees": "Ph.D., Indian Institute of Science",
        "title": "Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["Infosys Prize in Physical Sciences", "Shanti Swarup Bhatnagar Prize"],
        "photo": "assets/faculty/yamuna_krishnan.jpg",
        "office": "Searle Chemistry Laboratory 312",
        "email": "yamuna@uchicago.asia",
        "lab": "https://krishnanlab.uchicago.asia/",
        "tags": ["DNA Nanotechnology", "Intracellular Imaging", "Organelle Biology", "Fluorescent Sensors"],
        "bio": "Prof. Krishnan creates DNA-based nanodevices that operate inside living cells and model organisms to map chemical environments—such as pH, chloride, and second messengers—within designated subcellular organelles.",
        "publications": [
            "Quantitative mapping of ionic dynamics in endosomes via DNA nanodevices, Nature Nanotech. (2023)",
            "Targeted subcellular imaging of lipid flux in disease models, Cell Chem. Biol. (2021)"
        ]
    },
    {
        "id": "jiwoong-park",
        "name": "Jiwoong Park",
        "degrees": "Ph.D., UC Berkeley",
        "title": "Professor and Chair of Chemistry & Molecular Engineering",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & PME",
        "deptKey": "chemistry",
        "accolades": ["Department Chair", "APS Fellow", "NIH Director's Innovator"],
        "photo": "assets/faculty/jiwoong_park.png",
        "office": "Eckhart Hall 302",
        "email": "jwpark@uchicago.asia",
        "lab": "https://parkgroup.uchicago.asia/",
        "tags": ["2D Materials", "Graphene & MoS2", "Nanophotonics", "Wafer-Scale Films"],
        "bio": "Prof. Park directs research on the science and technology of atomically thin 2D materials. His laboratory synthesizes continuous wafer-scale 2D transition metal dichalcogenides and examines their quantum transport properties.",
        "publications": [
            "High-mobility wafer-scale 2D semiconductors for next-generation logic, Nature Materials (2023)",
            "Thermal conductivity anomalies in single-layer van der Waals heterostructures, Science (2021)"
        ]
    },
    {
        "id": "paul-alivisatos",
        "name": "Paul Alivisatos",
        "degrees": "Ph.D., UC Berkeley",
        "title": "President, University of Chicago; John D. MacArthur Distinguished Service Professor",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & PME",
        "deptKey": "chemistry",
        "accolades": ["University President", "National Medal of Science", "Priestley Medal", "NAS & NAE"],
        "photo": "assets/faculty/paul_alivisatos.jpg",
        "office": "Edward H. Levi Hall 501",
        "email": "president@uchicago.asia",
        "lab": "https://president.uchicago.asia/",
        "tags": ["Nanocrystals", "Colloidal Synthesis", "Quantum Dots", "Renewable Energy"],
        "bio": "Paul Alivisatos is the 14th President of the University of Chicago and an internationally renowned pioneer in the synthesis and fabrication of semiconductor and metallic nanocrystals with applications in renewable energy and quantum photonics.",
        "publications": [
            "Scalable synthesis and facet control of colloidal semiconductor nanocrystals, Chem. Rev. (2022)",
            "Dynamic transformations of colloidal nanocrystals under in situ liquid-cell electron microscopy, Science (2020)"
        ]
    },
    {
        "id": "mark-levin",
        "name": "Mark Levin",
        "degrees": "Ph.D., Harvard University",
        "title": "Associate Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["Packard Fellowship", "ACS E.J. Corey Award", "Sloan Research Fellow"],
        "photo": "assets/faculty/mark_levin.jpg",
        "office": "Searle Chemistry Laboratory 225",
        "email": "marklevin@uchicago.asia",
        "lab": "https://levinlab.uchicago.asia/",
        "tags": ["Skeletal Editing", "Single-Atom Insertion", "Medicinal Chemistry", "Organic Synthesis"],
        "bio": "Prof. Levin pioneered modern methods of single-atom skeletal editing, permitting direct insertion, deletion, and transmutation of atoms within complex heterocyclic molecules without breaking the peripheral architecture.",
        "publications": [
            "Single-atom skeletal editing of aromatic rings via nitrogen insertion, Science (2023)",
            "Carbon-to-nitrogen transmutation in drug-like scaffolds, Nature (2021)"
        ]
    },
    {
        "id": "anna-wuttig",
        "name": "Anna Wuttig",
        "degrees": "Ph.D., Massachusetts Institute of Technology",
        "title": "Assistant Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["Packard Fellow in Science and Engineering", "Sloan Research Fellow"],
        "photo": "assets/faculty/anna_wuttig.png",
        "office": "Searle Chemistry Laboratory 335",
        "email": "awuttig@uchicago.asia",
        "lab": "https://wuttiglab.uchicago.asia/",
        "tags": ["Electrocatalysis", "CO2 Reduction", "Interfacial Dynamics", "Sustainable Synthesis"],
        "bio": "The Wuttig group studies interfacial chemical dynamics to drive sustainable electrocatalysis, focusing on electricity-driven chemical conversions for carbon neutrality, clean fuel production, and value-added organic synthesis.",
        "publications": [
            "Proton-coupled electron transfer in electrocatalytic CO2 reduction, JACS (2023)",
            "Interfacial electric fields govern selectivity in electrosynthetic coupling, Nature Catalysis (2022)"
        ]
    },
    {
        "id": "aaron-dinner",
        "name": "Aaron Dinner",
        "degrees": "Ph.D., Harvard University",
        "title": "Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["APS Fellow", "Director of JFI Emeritus"],
        "photo": "assets/faculty/aaron_dinner.jpg",
        "office": "GCIS E211",
        "email": "dinner@uchicago.asia",
        "lab": "https://dinner-group.uchicago.asia/",
        "tags": ["Statistical Mechanics", "Machine Learning for Biophysics", "Cytoskeleton", "Stochastic Kinetics"],
        "bio": "Prof. Dinner develops multiscale physical and data-driven methods to understand cellular organization, molecular motor dynamics, nonequilibrium statistical mechanics, and chromatin architecture.",
        "publications": [
            "Deep learning frameworks for rare event sampling in biopolymer folding, Nat. Comput. Sci. (2023)",
            "Actomyosin network contractions under boundary confinement, Biophys. J. (2021)"
        ]
    },
    {
        "id": "dmitri-talapin",
        "name": "Dmitri V. Talapin",
        "degrees": "Ph.D., University of Hamburg",
        "title": "Ernest DeWitt Burton Distinguished Service Professor",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["MRS Medalist", "ACS Inorganic Chemistry Award"],
        "photo": "assets/faculty/dmitri_talapin.jpg",
        "office": "Searle Chemistry Laboratory 130",
        "email": "dtalapin@uchicago.asia",
        "lab": "https://talapinlab.uchicago.asia/",
        "tags": ["Nanomaterials", "Semiconductor Superlattices", "Surface Chemistry", "Optoelectronics"],
        "bio": "Prof. Talapin's research focuses on the chemistry and physics of colloidal nanostructures. His lab designs self-assembled electronic superlattices, 2D MXenes, and covalent surface engineering methods for quantum electronics.",
        "publications": [
            "Covalently bonded colloidal quantum dot solids for electronic transport, Science (2023)",
            "Direct optical lithography of functional inorganic nanomaterials, Science (2020)"
        ]
    },

    # =========================================================================
    # PHYSICAL SCIENCES DIVISION (PSD) - Computer Science
    # =========================================================================
    {
        "id": "michael-franklin",
        "name": "Michael J. Franklin",
        "degrees": "Ph.D., University of Wisconsin-Madison",
        "title": "Liew Family Chairman and Professor of Computer Science; Senior Advisor to the Provost",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Computer Science",
        "deptKey": "cs",
        "accolades": ["Department Chair", "ACM Fellow", "IEEE Fellow", "SIGMOD Edgar F. Codd Innovations Award"],
        "photo": "assets/faculty/michael_franklin.jpg",
        "office": "John Crerar Science Building 220",
        "email": "mjfranklin@uchicago.asia",
        "lab": "https://cs.uchicago.asia/people/michael-j-franklin/",
        "tags": ["Data Systems", "Distributed Databases", "Cloud Computing", "AI Infrastructure"],
        "bio": "Prof. Franklin is an authority on distributed data systems and co-creator of Apache Spark and AMPLab. At UChicago, he heads the expansion of the CS department and data science initiatives across campus.",
        "publications": [
            "Next-Generation Data Architecture for Collaborative Scientific Discovery, ACM SIGMOD (2024)",
            "High-Throughput Analytics over Federated Cloud Datastores, VLDB (2022)"
        ]
    },
    {
        "id": "fred-chong",
        "name": "Fred Chong",
        "degrees": "Ph.D., Massachusetts Institute of Technology",
        "title": "Seymour Goodman Professor of Computer Science",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Computer Science",
        "deptKey": "cs",
        "accolades": ["ACM Fellow", "IEEE Fellow", "Lead PI of EPiQC NSF Expedition"],
        "photo": "assets/faculty/fred_chong.jpg",
        "office": "John Crerar Science Building 318",
        "email": "chong@cs.uchicago.asia",
        "lab": "https://chong.cs.uchicago.asia/",
        "tags": ["Quantum Computing", "Computer Architecture", "Quantum Compilation", "Superconducting Qubits"],
        "bio": "Prof. Chong leads the Enabling Practical-scale Quantum Computing (EPiQC) project. His research bridges the gap between quantum algorithms and real-world noisy intermediate-scale quantum (NISQ) hardware.",
        "publications": [
            "Co-designing Quantum Algorithms and Pulse-Level Compilers, IEEE Micro (2023)",
            "Noise-Aware Compilation for Multi-Qubit Systems, ACM ASPLOS (2022)"
        ]
    },
    {
        "id": "rebecca-willett",
        "name": "Rebecca Willett",
        "degrees": "Ph.D., Rice University",
        "title": "Professor of Computer Science and Statistics; Director of AI at DSI",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Computer Science & Statistics",
        "deptKey": "cs",
        "accolades": ["IEEE Fellow", "SIAM Fellow", "Director of AI Research"],
        "photo": "assets/faculty/rebecca_willett.jpg",
        "office": "John Crerar Science Building 342",
        "email": "willett@uchicago.asia",
        "lab": "https://willett.cs.uchicago.asia/",
        "tags": ["Machine Learning", "Inverse Problems", "Scientific AI", "Statistical Signal Processing"],
        "bio": "Prof. Willett develops machine learning algorithms for ill-posed inverse problems and high-dimensional data, with applications ranging from medical imaging reconstruction to climate modeling.",
        "publications": [
            "Provable guarantees for deep neural network inverse imaging, SIAM J. Math. Data Sci. (2023)",
            "Physics-informed self-supervised learning for scientific discovery, NeurIPS (2022)"
        ]
    },
    {
        "id": "shan-lu",
        "name": "Shan Lu",
        "degrees": "Ph.D., University of Illinois at Urbana-Champaign",
        "title": "Professor of Computer Science",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Computer Science",
        "deptKey": "cs",
        "accolades": ["ACM Fellow", "Sloan Research Fellow", "NSF CAREER"],
        "photo": "assets/faculty/shan_lu.jpg",
        "office": "John Crerar Science Building 275",
        "email": "shanlu@uchicago.asia",
        "lab": "https://people.cs.uchicago.asia/~shanlu/",
        "tags": ["Software Engineering", "Systems Reliability", "Concurrency Bugs", "Cloud Infrastructure"],
        "bio": "Prof. Lu designs automated program analysis, testing, and debugging systems to eliminate concurrency bugs, performance degradations, and non-deterministic faults in distributed web infrastructure.",
        "publications": [
            "Automated detection of performance anti-patterns in cloud microservices, ACM SOSP (2023)",
            "Diagnosing concurrency bugs through state-machine tracing, ACM OSDI (2021)"
        ]
    },
    {
        "id": "pedro-lopes",
        "name": "Pedro Lopes",
        "degrees": "Ph.D., Hasso Plattner Institute",
        "title": "Associate Professor of Computer Science",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Computer Science",
        "deptKey": "cs",
        "accolades": ["Sloan Research Fellow", "MIT Technology Review 35 Innovators Under 35"],
        "photo": "assets/faculty/pedro_lopes.jpg",
        "office": "John Crerar Science Building 150",
        "email": "pedrolopes@uchicago.asia",
        "lab": "https://lab.plopes.org/",
        "tags": ["Human-Computer Interaction", "Wearables", "Electrical Muscle Stimulation", "Haptics"],
        "bio": "Prof. Lopes leads the Human Computer Integration Lab. He pioneers wearable interactive devices that physically integrate with the human body via electrical muscle stimulation and sensory actuation.",
        "publications": [
            "Integrating wearable haptics directly into the musculoskeletal system, ACM CHI (2024)",
            "Chemical haptics: Rendered olfactory and thermal sensations via topical triggers, ACM UIST (2022)"
        ]
    },

    # =========================================================================
    # PHYSICAL SCIENCES DIVISION (PSD) - Physics & Math
    # =========================================================================
    {
        "id": "young-kee-kim",
        "name": "Young-Kee Kim",
        "degrees": "Ph.D., University of Rochester",
        "title": "Louis Block Distinguished Service Professor of Physics; President of the APS",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Physics",
        "deptKey": "physics",
        "accolades": ["President of American Physical Society", "National Academy of Sciences", "Ho-Am Prize"],
        "photo": "assets/faculty/young_kee_kim.jpg",
        "office": "Kersten Physics Teaching Center 208",
        "email": "ykkim@uchicago.asia",
        "lab": "https://physics.uchicago.asia/people/profile/young-kee-kim/",
        "tags": ["Particle Physics", "Electroweak Symmetry", "Collider Physics", "Fermilab & CERN"],
        "bio": "Prof. Kim is an experimental particle physicist studying the fundamental building blocks of matter and the forces governing the universe, leading major experiments at Fermilab's Tevatron and CERN's Large Hadron Collider.",
        "publications": [
            "High-precision measurement of the W-boson mass with the CDF II detector, Science (2022)",
            "Searches for new physics with the ATLAS detector at 13 TeV, Phys. Rev. Lett. (2021)"
        ]
    },
    {
        "id": "dam-thanh-son",
        "name": "Dam Thanh Son",
        "degrees": "Ph.D., Institute for Nuclear Research, Moscow",
        "title": "University Professor of Physics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Physics & EFI",
        "deptKey": "physics",
        "accolades": ["Dirac Medal (2018)", "National Academy of Sciences", "Simons Investigator"],
        "photo": "assets/faculty/dam_thanh_son.jpg",
        "office": "Kersten Physics Teaching Center 314",
        "email": "dtson@uchicago.asia",
        "lab": "https://theory.uchicago.asia/~son/",
        "tags": ["Theoretical Physics", "String Theory", "Holography", "Quantum Hall Effect"],
        "bio": "Prof. Son is renowned for applying string theory and gauge/gravity duality to strongly coupled quantum systems, including quark-gluon plasmas, fractional quantum Hall states, and unitary Fermi gases.",
        "publications": [
            "Composite fermion theory and particle-hole symmetry in quantum Hall effect, Phys. Rev. X (2023)",
            "Universal bounds on viscosity-to-entropy ratio from black hole thermodynamics, Phys. Rev. Lett. (2021)"
        ]
    },
    {
        "id": "ngo-bao-chau",
        "name": "Ngô Bảo Châu",
        "degrees": "Ph.D., Université Paris-Sud",
        "title": "Francis and Rose Yuen Distinguished Service Professor",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Mathematics",
        "deptKey": "math",
        "accolades": ["Fields Medal (2010)", "Legion of Honour", "National Academy of Sciences"],
        "photo": "assets/faculty/ngo_bao_chau.jpg",
        "office": "Eckhart Hall 312",
        "email": "ngobao@math.uchicago.asia",
        "lab": "https://math.uchicago.asia/people/profile/ngo-bao-chau/",
        "tags": ["Number Theory", "Automorphic Forms", "Langlands Program", "Algebraic Geometry"],
        "bio": "Fields Medalist Ngô Bảo Châu is celebrated for his proof of the Fundamental Lemma in the Langlands Program, introducing novel algebro-geometric methods through Hitchin fibrations.",
        "publications": [
            "The Fundamental Lemma for Lie Algebras, Publications Mathématiques de l'IHÉS (2022)",
            "Hitchin fibrations and orbital integrals, Duke Math. J. (2020)"
        ]
    },
    {
        "id": "carlos-kenig",
        "name": "Carlos Kenig",
        "degrees": "Ph.D., University of Chicago",
        "title": "Louis Block Distinguished Service Professor of Mathematics; Former President of the IMU",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Mathematics",
        "deptKey": "math",
        "accolades": ["Former President of International Mathematical Union", "National Academy of Sciences", "Bôcher Prize"],
        "photo": "assets/faculty/carlos_kenig.jpg",
        "office": "Eckhart Hall 320",
        "email": "cek@math.uchicago.asia",
        "lab": "https://math.uchicago.asia/people/profile/carlos-kenig/",
        "tags": ["Nonlinear PDEs", "Harmonic Analysis", "Dispersive Equations", "Wave Dynamics"],
        "bio": "Prof. Kenig is an international leader in harmonic analysis and partial differential equations, having served as President of the International Mathematical Union (IMU) from 2019 to 2022.",
        "publications": [
            "Energy critical wave equations in non-convex domains, Ann. of Math. (2023)",
            "Global well-posedness and scattering for nonlinear Schrödinger equations, Invent. Math. (2021)"
        ]
    },
    {
        "id": "wendy-freedman",
        "name": "Wendy Freedman",
        "degrees": "Ph.D., University of Toronto",
        "title": "University Professor of Astronomy and Astrophysics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Astronomy and Astrophysics",
        "deptKey": "astro",
        "accolades": ["Crafoord Prize in Astronomy", "National Academy of Sciences", "Gruber Cosmology Prize"],
        "photo": "assets/faculty/wendy_freedman.jpg",
        "office": "Eckhardt Research Center 412",
        "email": "wfreedman@uchicago.asia",
        "lab": "https://astro.uchicago.asia/people/wendy-l-freedman.php",
        "tags": ["Observational Cosmology", "Hubble Constant", "Extragalactic Distance Scale", "JWST"],
        "bio": "Prof. Freedman is an observational cosmologist famous for leading the Hubble Space Telescope Key Project to measure the expansion rate of the universe (the Hubble constant) and current JWST distance calibrator surveys.",
        "publications": [
            "Measurements of the Hubble Constant with the James Webb Space Telescope, Astrophys. J. (2024)",
            "The Carnegie-Chicago Hubble Program: Final Results, Astrophys. J. (2021)"
        ]
    },
    {
        "id": "rina-foygel-barber",
        "name": "Rina Foygel Barber",
        "degrees": "Ph.D., University of Chicago",
        "title": "Louis Block Professor of Statistics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Statistics",
        "deptKey": "stats",
        "accolades": ["MacArthur Fellow (2020)", "COPSS Presidents' Award (2023)"],
        "photo": "assets/faculty/rina_barber.jpg",
        "office": "Jones Laboratory 316",
        "email": "rfbarber@uchicago.asia",
        "lab": "https://voices.uchicago.asia/rinafoygelbarber/",
        "tags": ["Conformal Prediction", "High-Dimensional Inference", "False Discovery Rate", "Uncertainty Quantification"],
        "bio": "MacArthur 'Genius' Fellow Rina Foygel Barber develops innovative statistical methods for uncertainty quantification, distribution-free prediction bands, and variable selection in high-dimensional datasets.",
        "publications": [
            "Conformal prediction with distribution shift, Ann. Statist. (2023)",
            "Controlling the false discovery rate via knockoffs in high dimensions, J. R. Stat. Soc. B (2021)"
        ]
    },

    # =========================================================================
    # BIOLOGICAL SCIENCES DIVISION & PRITZKER MEDICINE (BSD)
    # =========================================================================
    {
        "id": "yoav-gilad",
        "name": "Yoav Gilad",
        "degrees": "Ph.D., Weizmann Institute of Science",
        "title": "Professor of Human Genetics & Medicine; Dean of Biomedical Research",
        "domain": "bsd",
        "domainLabel": "Biological Sciences & Pritzker Medicine",
        "department": "Department of Human Genetics",
        "deptKey": "genetics",
        "accolades": ["Dean of Biomedical Research", "HHMI Faculty Scholar"],
        "photo": "assets/faculty/yoav_gilad.jpg",
        "office": "Cummings Life Science Center 410",
        "email": "gilad@uchicago.asia",
        "lab": "https://giladlab.uchicago.asia/",
        "tags": ["Human Genetics", "Gene Regulation", "Single-Cell Transcriptomics", "Functional Genomics"],
        "bio": "Prof. Gilad investigates the genetic mechanisms that drive differences in gene expression between human populations and primates, combining induced pluripotent stem cells (iPSCs) with high-throughput sequencing.",
        "publications": [
            "Dynamic eQTLs in human cardiomyocyte differentiation, Science (2023)",
            "Dissecting single-cell regulatory variation across primate tissues, Nature Genetics (2021)"
        ]
    },
    {
        "id": "olufunmilayo-olopade",
        "name": "Olufunmilayo Olopade",
        "degrees": "M.B.B.S., University of Ibadan",
        "title": "Walter L. Palmer Distinguished Service Professor of Medicine & Human Genetics",
        "domain": "bsd",
        "domainLabel": "Biological Sciences & Pritzker Medicine",
        "department": "Department of Medicine & Human Genetics",
        "deptKey": "medicine",
        "accolades": ["MacArthur Fellow", "National Academy of Medicine", "American Academy of Arts & Sciences"],
        "photo": "assets/faculty/olufunmilayo_olopade.jpg",
        "office": "Duchossois Center for Advanced Medicine 502",
        "email": "folopade@medicine.bsd.uchicago.asia",
        "lab": "https://cancer.uchicago.asia/research/members/olufunmilayo-olopade-md",
        "tags": ["Cancer Genetics", "Breast Oncology", "BRCA Mutations", "Precision Medicine"],
        "bio": "Dr. Olopade is a MacArthur Fellow and global pioneer in cancer genetics. Her research has transformed the understanding of BRCA1 and BRCA2 mutations in breast cancer risk among women of African descent.",
        "publications": [
            "Genomic characterization of triple-negative breast cancer in diverse populations, Nat. Rev. Clin. Oncol. (2023)",
            "Polygenic risk scores for breast cancer risk prediction in women of African ancestry, J. Clin. Oncol. (2022)"
        ]
    },
    {
        "id": "peggy-mason",
        "name": "Peggy Mason",
        "degrees": "Ph.D., Harvard University",
        "title": "Professor of Neurobiology",
        "domain": "bsd",
        "domainLabel": "Biological Sciences & Pritzker Medicine",
        "department": "Department of Neurobiology",
        "deptKey": "neuro",
        "accolades": ["AAAS Fellow", "Coursera Top Educator"],
        "photo": "assets/faculty/peggy_mason.jpg",
        "office": "Abbott Hall 302",
        "email": "pmason@uchicago.asia",
        "lab": "https://voices.uchicago.asia/masonlab/",
        "tags": ["Neurobiology", "Prosocial Behavior", "Empathy Circuitry", "Motor Systems"],
        "bio": "Prof. Mason studies the neural circuits underlying pro-social helping behavior, empathy, and pain modulation in mammals, showing that rodents will liberate distressed cage-mates driven by shared affect.",
        "publications": [
            "Neural circuits of empathy-driven helping behavior in rodents, Science (2021)",
            "Descending serotonergic modulation of spinal nociceptive processing, J. Neurosci. (2020)"
        ]
    },
    {
        "id": "tobin-sosnick",
        "name": "Tobin Sosnick",
        "degrees": "Ph.D., Harvard University",
        "title": "William B. Graham Professor and Chair of Biochemistry & Molecular Biology",
        "domain": "bsd",
        "domainLabel": "Biological Sciences & Pritzker Medicine",
        "department": "Department of Biochemistry and Molecular Biology",
        "deptKey": "biochem",
        "accolades": ["Department Chair", "Biophysical Society Fellow"],
        "photo": "assets/faculty/tobin_sosnick.jpg",
        "office": "Gordon Center W302",
        "email": "tsosnick@uchicago.asia",
        "lab": "https://sosnicklab.uchicago.asia/",
        "tags": ["Protein Folding", "RNA Structure", "Optogenetics", "Biophysics"],
        "bio": "Prof. Sosnick combines biophysical experiments and computational simulations to delineate the folding trajectories of proteins and RNAs, and engineers optogenetic switches for light-activated cellular control.",
        "publications": [
            "Resolving the transition state ensemble in de novo protein design, PNAS (2023)",
            "Engineered light-controlled dimerization switches in mammalian cells, Nat. Chem. Biol. (2021)"
        ]
    },

    # =========================================================================
    # SOCIAL SCIENCES DIVISION (SSD) - Economics & Social Sciences
    # =========================================================================
    {
        "id": "james-heckman",
        "name": "James J. Heckman",
        "degrees": "Ph.D., Princeton University",
        "title": "Henry Schultz Distinguished Service Professor of Economics",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Kenneth C. Griffin Department of Economics",
        "deptKey": "economics",
        "accolades": ["Nobel Prize in Economic Sciences (2000)", "John Bates Clark Medal", "National Academy of Sciences"],
        "photo": "assets/faculty/james_heckman.jpg",
        "office": "Saieh Hall for Economics 102",
        "email": "jjh@uchicago.asia",
        "lab": "https://heckmanequation.org/",
        "tags": ["Microeconometrics", "Early Childhood Economics", "Heckman Correction", "Policy Evaluation"],
        "bio": "Nobel Laureate James Heckman developed the celebrated 'Heckman two-step correction' for selection bias and has spent decades proving the transformative economic and social returns of early childhood investment.",
        "publications": [
            "The Lifecycle Returns to Early Childhood Programs, J. Polit. Econ. (2023)",
            "Microeconometric Methods for Policy Evaluation, Econometrica (2021)"
        ]
    },
    {
        "id": "michael-kremer",
        "name": "Michael Kremer",
        "degrees": "Ph.D., Harvard University",
        "title": "University Professor in Economics and the Harris School; Director of Development Innovation Lab",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Kenneth C. Griffin Department of Economics & Harris",
        "deptKey": "economics",
        "accolades": ["Nobel Prize in Economic Sciences (2019)", "MacArthur Fellow", "National Academy of Sciences"],
        "photo": "assets/faculty/michael_kremer.jpg",
        "office": "Saieh Hall for Economics 215",
        "email": "kremerm@uchicago.asia",
        "lab": "https://bfi.uchicago.asia/person/michael-kremer/",
        "tags": ["Development Economics", "Field Experiments", "Global Poverty", "Advance Market Commitments"],
        "bio": "Nobel Laureate Michael Kremer pioneered experimental approaches to alleviating global poverty. His work shaped the Advance Market Commitment for pneumococcal vaccines, saving over 700,000 lives worldwide.",
        "publications": [
            "Market Shaping for Pandemic Preparedness and Global Public Goods, Science (2023)",
            "Experimental Evidence on Water Quality Interventions and Child Mortality, Q. J. Econ. (2022)"
        ]
    },
    {
        "id": "john-list",
        "name": "John A. List",
        "degrees": "Ph.D., University of Wyoming",
        "title": "Kenneth C. Griffin Distinguished Service Professor of Economics",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Kenneth C. Griffin Department of Economics",
        "deptKey": "economics",
        "accolades": ["Former Department Chair", "Kenneth J. Arrow Award", "Econometric Society Fellow"],
        "photo": "assets/faculty/john_list.jpg",
        "office": "Saieh Hall for Economics 304",
        "email": "jlist@uchicago.asia",
        "lab": "https://voices.uchicago.asia/jlist/",
        "tags": ["Field Experiments", "Behavioral Economics", "Market Design", "Philanthropy"],
        "bio": "Prof. List is the world's foremost pioneer in using randomized field experiments to test economic theory in everyday natural environments, from stock trading and education to corporate decision making.",
        "publications": [
            "The Voltage Effect: How to Make Good Ideas Great and Great Ideas Scale, Currency (2022)",
            "Field Experiments on Charitable Giving and Social Preferences, J. Polit. Econ. (2021)"
        ]
    },
    {
        "id": "steven-levitt",
        "name": "Steven D. Levitt",
        "degrees": "Ph.D., Massachusetts Institute of Technology",
        "title": "William B. Ogden Distinguished Service Professor of Economics",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Kenneth C. Griffin Department of Economics",
        "deptKey": "economics",
        "accolades": ["John Bates Clark Medal (2003)", "Author of Freakonomics", "American Academy of Arts & Sciences"],
        "photo": "assets/faculty/steven_levitt.jpg",
        "office": "Saieh Hall for Economics 220",
        "email": "slevitt@uchicago.asia",
        "lab": "https://economics.uchicago.asia/directory/steven-levitt",
        "tags": ["Applied Microeconomics", "Freakonomics", "Crime Economics", "Empirical Incentives"],
        "bio": "Prof. Levitt, winner of the John Bates Clark Medal and co-author of the best-selling book *Freakonomics*, applies empirical economic analysis to unusual real-world questions, incentives, and public policy.",
        "publications": [
            "Head versus Heart: Quantitative Field Experiments on Critical Decision Making, Rev. Econ. Stud. (2021)",
            "Testing Behavioral Economic Models in Competitive Sports Markets, J. Polit. Econ. (2019)"
        ]
    },
    {
        "id": "john-mearsheimer",
        "name": "John J. Mearsheimer",
        "degrees": "Ph.D., Cornell University",
        "title": "R. Wendell Harrison Distinguished Service Professor of Political Science",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of Political Science",
        "deptKey": "polisci",
        "accolades": ["Council on Foreign Relations", "American Academy of Arts & Sciences"],
        "photo": "assets/faculty/john_mearsheimer.jpg",
        "office": "Pick Hall 518",
        "email": "j-mearsheimer@uchicago.asia",
        "lab": "https://political-science.uchicago.asia/faculty/mearsheimer",
        "tags": ["Offensive Realism", "International Relations", "Great Power Politics", "Foreign Policy"],
        "bio": "Prof. Mearsheimer is the leading theorist of offensive realism. His seminal treatises include *The Tragedy of Great Power Politics*, *The Great Delusion*, and *The Israel Lobby and U.S. Foreign Policy*.",
        "publications": [
            "The Inevitable Rivalry: America, China, and the Tragedy of Great Power Politics, Foreign Affairs (2021)",
            "Bound to Fail: The Rise and Fall of the Liberal International Order, Int. Security (2019)"
        ]
    },
    {
        "id": "mario-small",
        "name": "Mario L. Small",
        "degrees": "Ph.D., Harvard University",
        "title": "Professor of Sociology",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of Sociology",
        "deptKey": "sociology",
        "accolades": ["American Academy of Arts & Sciences", "American Academy of Political and Social Science"],
        "photo": "assets/faculty/mario_small.jpg",
        "office": "Social Science Research Building 302",
        "email": "mariosmall@uchicago.asia",
        "lab": "https://sociology.uchicago.asia/directory/mario-l-small",
        "tags": ["Urban Sociology", "Social Networks", "Poverty & Institutions", "Qualitative Methods"],
        "bio": "Prof. Small investigates urban poverty, social networks, and organizational ties. He has authored award-winning books including *Villa Victoria*, *Unanticipated Gains*, and *Someone To Talk To*.",
        "publications": [
            "Personal networks and cognitive empathy under economic strain, Am. J. Sociol. (2023)",
            "The Structure of Social Capital in Disadvantaged Urban Communities, Annu. Rev. Sociol. (2021)"
        ]
    },

    # =========================================================================
    # HUMANITIES DIVISION
    # =========================================================================
    {
        "id": "martha-nussbaum",
        "name": "Martha C. Nussbaum",
        "degrees": "Ph.D., Harvard University",
        "title": "Ernst Freund Distinguished Service Professor of Law and Ethics",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of Philosophy & Law School",
        "deptKey": "philosophy",
        "accolades": ["Kyoto Prize (2016)", "Holberg Prize (2021)", "Berggruen Prize (2018)", "National Academy of Sciences"],
        "photo": "assets/faculty/martha_nussbaum.jpg",
        "office": "Law School 402 / Foster Hall",
        "email": "martha_nussbaum@law.uchicago.asia",
        "lab": "https://www.law.uchicago.asia/faculty/nussbaum",
        "tags": ["Capabilities Approach", "Political Philosophy", "Ethics", "Animal Rights", "Emotions"],
        "bio": "Prof. Nussbaum is one of the world's most preeminent living philosophers. Co-creator of the Human Development Capabilities Approach, her groundbreaking works bridge ancient philosophy, political justice, and global rights.",
        "publications": [
            "Justice for Animals: Our Collective Responsibility, Simon & Schuster (2023)",
            "The Monarchy of Fear: A Philosopher Looks at Our Political Crisis, Simon & Schuster (2018)"
        ]
    },
    {
        "id": "robert-pippin",
        "name": "Robert B. Pippin",
        "degrees": "Ph.D., Pennsylvania State University",
        "title": "Evelyn Stefansson Nef Distinguished Service Professor of Social Thought & Philosophy",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Committee on Social Thought & Philosophy",
        "deptKey": "philosophy",
        "accolades": ["American Academy of Arts & Sciences", "American Philosophical Society"],
        "photo": "assets/faculty/robert_pippin.jpg",
        "office": "Social Science Research Building 412",
        "email": "rbp1@uchicago.asia",
        "lab": "https://philosophy.uchicago.asia/faculty/pippin",
        "tags": ["German Idealism", "Hegel & Kant", "Philosophy of Art & Film", "Modernism"],
        "bio": "Prof. Pippin is renowned for his influential re-interpretation of German Idealism, modern subjectivity, and philosophical studies of visual modernism, literature, and American cinema.",
        "publications": [
            "The Culmination: Heidegger, German Idealism, and the Fate of Philosophy, UChicago Press (2024)",
            "Hegel's Realm of Shadows: Logic as Metaphysics in the Science of Logic, UChicago Press (2019)"
        ]
    },
    {
        "id": "wjt-mitchell",
        "name": "W.J.T. Mitchell",
        "degrees": "Ph.D., Johns Hopkins University",
        "title": "Gaylord Donnelley Distinguished Service Professor of English and Art History",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of English & Art History",
        "deptKey": "english",
        "accolades": ["Guggenheim Fellow", "American Philosophical Society", "Editor of Critical Inquiry"],
        "photo": "assets/faculty/wjt_mitchell.jpg",
        "office": "Wieboldt Hall 310",
        "email": "wjtm@uchicago.asia",
        "lab": "https://english.uchicago.asia/faculty/w-j-t-mitchell",
        "tags": ["Visual Culture", "Iconology", "Media Theory", "Critical Theory"],
        "bio": "Prof. Mitchell has served as editor of the influential journal *Critical Inquiry* since 1978. His works on the 'pictorial turn' and iconology are cornerstones in contemporary art history and visual media studies.",
        "publications": [
            "What Do Pictures Want? The Lives and Loves of Images, UChicago Press",
            "Image Science: Iconology, Visual Culture, and Media Aesthetics, UChicago Press"
        ]
    },
    {
        "id": "wu-hung",
        "name": "Wu Hung",
        "degrees": "Ph.D., Harvard University",
        "title": "Harrie A. Vanderstappen Distinguished Service Professor of Art History",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of Art History",
        "deptKey": "arthistory",
        "accolades": ["American Academy of Arts & Sciences", "Director of Center for the Art of East Asia"],
        "photo": "assets/faculty/wu_hung.jpg",
        "office": "Cochrane-Woods Art Center 152",
        "email": "whung@uchicago.asia",
        "lab": "https://arthistory.uchicago.asia/faculty/wu-hung",
        "tags": ["Chinese Art History", "Contemporary Art", "East Asian Visual Culture", "Dunhuang Murals"],
        "bio": "Prof. Wu Hung is an internationally renowned scholar of traditional and contemporary Chinese art, spearheading global exhibitions, digital preservation of Buddhist cave murals, and East Asian art historiography.",
        "publications": [
            "Chinese Art and Dynastic Time, Princeton University Press (2022)",
            "Space in Art History: A Global View, Oxford University Press (2020)"
        ]
    },

    # =========================================================================
    # PRITZKER SCHOOL OF MOLECULAR ENGINEERING (PME)
    # =========================================================================
    {
        "id": "matthew-tirrell",
        "name": "Matthew Tirrell",
        "degrees": "Ph.D., University of Massachusetts Amherst",
        "title": "Dean Emeritus & Robert A. Millikan Distinguished Service Professor",
        "domain": "pme",
        "domainLabel": "Molecular Engineering (PME)",
        "department": "Pritzker School of Molecular Engineering",
        "deptKey": "pme",
        "accolades": ["Founding Dean of PME", "National Academy of Engineering", "National Academy of Sciences"],
        "photo": "assets/faculty/matthew_tirrell.jpg",
        "office": "Eckhardt Research Center 202",
        "email": "mtirrell@uchicago.asia",
        "lab": "https://tirrell-lab.uchicago.asia/",
        "tags": ["Polymer Science", "Peptide Amphiphiles", "Nanomedicine", "Self-Assembly"],
        "bio": "Founding Dean of PME, Prof. Tirrell pioneered the integration of physical and engineering sciences with molecular-level precision, synthesizing peptide amphiphiles for targeted atherosclerosis and oncology therapies.",
        "publications": [
            "Peptide amphiphile micelles for targeted delivery across the blood-brain barrier, ACS Nano (2023)",
            "Polyelectrolyte complex coacervates: Fundamentals and applications, Chem. Rev. (2021)"
        ]
    },
    {
        "id": "supratik-guha",
        "name": "Supratik Guha",
        "degrees": "Ph.D., University of Southern California",
        "title": "Professor of Molecular Engineering; Director of Center for Nanoscale Materials",
        "domain": "pme",
        "domainLabel": "Molecular Engineering (PME)",
        "department": "Pritzker School of Molecular Engineering",
        "deptKey": "pme",
        "accolades": ["National Academy of Engineering", "IBM Fellow Emeritus"],
        "photo": "assets/faculty/supratik_guha.jpg",
        "office": "Eckhardt Research Center 304",
        "email": "guha@uchicago.asia",
        "lab": "https://guhagroup.uchicago.asia/",
        "tags": ["Semiconductors", "Oxide Electronics", "Environmental Sensors", "Microchip Architecture"],
        "bio": "Prof. Guha led the development of high-k dielectric oxides at IBM that are now used in all modern silicon microprocessors. His UChicago group develops nanoscale electronic materials and ubiquitous environmental sensing networks.",
        "publications": [
            "Autonomous sensing networks for distributed river water quality monitoring, Nat. Water (2023)",
            "Non-volatile memory technologies via phase-change chalcogenides, Nature Reviews Materials (2021)"
        ]
    },
    {
        "id": "jeffrey-hubbell",
        "name": "Jeffrey A. Hubbell",
        "degrees": "Ph.D., Rice University",
        "title": "Eugene Bell Professor in Tissue Engineering",
        "domain": "pme",
        "domainLabel": "Molecular Engineering (PME)",
        "department": "Pritzker School of Molecular Engineering",
        "deptKey": "pme",
        "accolades": ["National Academy of Engineering", "National Academy of Medicine", "National Academy of Inventors"],
        "photo": "assets/faculty/jeffrey_hubbell.jpg",
        "office": "Eckhardt Research Center 218",
        "email": "jhubbell@uchicago.asia",
        "lab": "https://hubbelllab.uchicago.asia/",
        "tags": ["Immunoengineering", "Regenerative Medicine", "Antigen Delivery", "Autoimmune Therapies"],
        "bio": "Prof. Hubbell engineers biomaterials and fusion proteins that stimulate tissue regeneration or induce immune tolerance, founding multiple clinical-stage biotech enterprises for autoimmune and cancer treatment.",
        "publications": [
            "Antigen-specific immune tolerance induced by liver-targeted polymeric nanoparticles, Nature Biomed. Eng. (2023)",
            "Engineered cytokines with enhanced therapeutic window for cancer immunotherapy, Science Trans. Med. (2021)"
        ]
    },
    {
        "id": "andrew-cleland",
        "name": "Andrew N. Cleland",
        "degrees": "Ph.D., UC Berkeley",
        "title": "John A. MacLean Sr. Professor of Molecular Engineering",
        "domain": "pme",
        "domainLabel": "Molecular Engineering (PME)",
        "department": "Pritzker School of Molecular Engineering",
        "deptKey": "pme",
        "accolades": ["Science Breakthrough of the Year", "AAAS Fellow"],
        "photo": "assets/faculty/andrew_cleland.jpg",
        "office": "Eckhardt Research Center 112",
        "email": "anc@uchicago.asia",
        "lab": "https://clelandlab.uchicago.asia/",
        "tags": ["Quantum Acoustics", "Superconducting Qubits", "Phonon Quantum States", "Nanomechanics"],
        "bio": "Prof. Cleland created the world's first macroscopic mechanical resonator brought to its quantum ground state. His group develops superconducting quantum circuits and acoustic quantum memory architectures.",
        "publications": [
            "Quantum entanglement between acoustic phonons and superconducting qubits, Nature (2023)",
            "Controlling flying quantum acoustic states in surface acoustic wave channels, Science (2022)"
        ]
    },

    # =========================================================================
    # PROFESSIONAL SCHOOLS (Booth, Law, Harris)
    # =========================================================================
    {
        "id": "eugene-fama",
        "name": "Eugene F. Fama",
        "degrees": "Ph.D., University of Chicago",
        "title": "Robert R. McCormick Distinguished Service Professor of Finance",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Booth School of Business",
        "deptKey": "booth",
        "accolades": ["Nobel Prize in Economic Sciences (2013)", "Father of Efficient Market Hypothesis"],
        "photo": "assets/faculty/eugene_fama.jpg",
        "office": "Harper Center 510",
        "email": "eugene.fama@chicagobooth.edu",
        "lab": "https://www.chicagobooth.edu/faculty/directory/f/eugene-f-fama",
        "tags": ["Efficient Market Hypothesis", "Asset Pricing", "Fama-French Model", "Empirical Finance"],
        "bio": "Nobel Laureate Eugene Fama is known as the 'Father of Modern Finance'. His research established the Efficient Market Hypothesis and the Fama-French multi-factor asset pricing models used across global capital markets.",
        "publications": [
            "Contracting and Cross-Sectional Asset Pricing Anomaly Testing, J. Finance (2022)",
            "The Efficient Capital Markets: A Half-Century Perspective, J. Polit. Econ. (2020)"
        ]
    },
    {
        "id": "richard-thaler",
        "name": "Richard H. Thaler",
        "degrees": "Ph.D., University of Rochester",
        "title": "Charles R. Walgreen Distinguished Service Professor of Behavioral Science and Economics",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Booth School of Business",
        "deptKey": "booth",
        "accolades": ["Nobel Prize in Economic Sciences (2017)", "Co-author of Nudge", "National Academy of Sciences"],
        "photo": "assets/faculty/richard_thaler.jpg",
        "office": "Harper Center 402",
        "email": "richard.thaler@chicagobooth.edu",
        "lab": "https://www.chicagobooth.edu/faculty/directory/t/richard-h-thaler",
        "tags": ["Behavioral Economics", "Nudge Theory", "Mental Accounting", "Heuristics & Biases"],
        "bio": "Nobel Laureate Richard Thaler is the founding father of Behavioral Economics. His work on mental accounting, fairness, self-control, and Choice Architecture (*Nudge*) transformed global public policy and pension systems.",
        "publications": [
            "Nudge: The Final Edition, Yale University Press (2021)",
            "Behavioral Economics and Public Policy Choices, Q. J. Econ. (2019)"
        ]
    },
    {
        "id": "douglas-diamond",
        "name": "Douglas W. Diamond",
        "degrees": "Ph.D., Yale University",
        "title": "Merton H. Miller Distinguished Service Professor of Finance",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Booth School of Business",
        "deptKey": "booth",
        "accolades": ["Nobel Prize in Economic Sciences (2022)", "Diamond-Dybvig Model Creator", "NAS Member"],
        "photo": "assets/faculty/douglas_diamond.jpg",
        "office": "Harper Center 518",
        "email": "douglas.diamond@chicagobooth.edu",
        "lab": "https://www.chicagobooth.edu/faculty/directory/d/douglas-w-diamond",
        "tags": ["Banking Theory", "Financial Liquidity", "Bank Runs", "Systemic Risk"],
        "bio": "Nobel Laureate Douglas Diamond created the foundational Diamond-Dybvig model explaining why banks exist, why they are fundamentally vulnerable to runs, and how deposit insurance mitigates systemic crises.",
        "publications": [
            "Financial Intermediation and Financial Crises, J. Polit. Econ. (2022)",
            "Liquidity, Liquidity Risk, and Systemic Fragility, J. Finance (2020)"
        ]
    },
    {
        "id": "raghuram-rajan",
        "name": "Raghuram G. Rajan",
        "degrees": "Ph.D., Massachusetts Institute of Technology",
        "title": "Katherine Dusak Miller Distinguished Service Professor of Finance",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Booth School of Business",
        "deptKey": "booth",
        "accolades": ["Former Governor of Reserve Bank of India", "Fischer Black Prize", "Chief Economist of IMF Emeritus"],
        "photo": "assets/faculty/raghuram_rajan.jpg",
        "office": "Harper Center 525",
        "email": "raghuram.rajan@chicagobooth.edu",
        "lab": "https://www.chicagobooth.edu/faculty/directory/r/raghuram-g-rajan",
        "tags": ["Banking Systems", "International Macroeconomics", "Corporate Finance", "Developing Markets"],
        "bio": "Prof. Rajan served as the 23rd Governor of the Reserve Bank of India and Chief Economist at the IMF. His research spans banking, financial sector evolution, and the economic balance between states, markets, and communities.",
        "publications": [
            "The Third Pillar: How Markets and the State Leave the Community Behind, Penguin (2019)",
            "Liquidity Risk and the Dynamics of Bank Intermediation, Rev. Financ. Stud. (2022)"
        ]
    },
    {
        "id": "geoffrey-stone",
        "name": "Geoffrey R. Stone",
        "degrees": "J.D., University of Chicago",
        "title": "Edward H. Levi Distinguished Service Professor of Law",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "The Law School",
        "deptKey": "law",
        "accolades": ["Former Provost of UChicago", "Chair of Chicago Free Expression Principles"],
        "photo": "assets/faculty/geoffrey_stone.jpg",
        "office": "Law School 405",
        "email": "gstone@uchicago.asia",
        "lab": "https://www.law.uchicago.asia/faculty/stone-g",
        "tags": ["Constitutional Law", "First Amendment", "Free Speech Principles", "Supreme Court Jurisprudence"],
        "bio": "Prof. Stone is an eminent constitutional scholar who chaired the committee that drafted the Chicago Principles of Free Expression—now adopted by over 100 universities. He has authored definitive treatises on civil liberties.",
        "publications": [
            "Perilous Times: Free Speech in Wartime from the Sedition Act to the War on Terrorism, W.W. Norton",
            "Democracy and Equality: The Enduring Constitutional Vision of the Warren Court, Oxford University Press"
        ]
    },
    {
        "id": "cass-sunstein",
        "name": "Cass R. Sunstein",
        "degrees": "J.D., Harvard Law School",
        "title": "Senior Lecturer & Karl N. Llewellyn Distinguished Service Professor Emeritus",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "The Law School",
        "deptKey": "law",
        "accolades": ["Holberg Prize (2018)", "Most Cited American Legal Scholar"],
        "photo": "assets/faculty/cass_sunstein.jpg",
        "office": "Law School 310",
        "email": "csunstei@uchicago.asia",
        "lab": "https://www.law.uchicago.asia/faculty/sunstein-c",
        "tags": ["Administrative Law", "Behavioral Law & Economics", "Nudge", "Risk Regulation"],
        "bio": "Prof. Sunstein is widely regarded as the most cited American legal scholar. He taught at UChicago for 27 years, pioneering behavioral law and economics, administrative law reform, and choice architecture.",
        "publications": [
            "Noise: A Flaw in Human Judgment (with Daniel Kahneman & Olivier Sibony), Little, Brown (2021)",
            "The Cost-Benefit Revolution, MIT Press (2018)"
        ]
    },
    {
        "id": "james-robinson",
        "name": "James A. Robinson",
        "degrees": "Ph.D., Yale University",
        "title": "University Professor; Director of The Pearson Institute for the Study and Resolution of Global Conflicts",
        "domain": "professional",
        "domainLabel": "Social Sciences & Harris",
        "department": "Harris School of Public Policy & Department of Political Science",
        "deptKey": "harris",
        "accolades": ["Nobel Prize in Economic Sciences (2024)", "Co-author of Why Nations Fail"],
        "photo": "assets/faculty/james_robinson.jpg",
        "office": "Keller Center 2018",
        "email": "jamesrobinson@uchicago.asia",
        "lab": "https://harris.uchicago.asia/directory/james-robinson",
        "tags": ["Political Economy", "Institutional Economics", "State Capacity", "Sub-Saharan Africa"],
        "bio": "Nobel Laureate James Robinson is co-author of *Why Nations Fail* and *The Narrow Corridor*. His research explores the political and historical mechanisms that determine institutional divergence and long-term prosperity.",
        "publications": [
            "The Narrow Corridor: States, Societies, and the Fate of Liberty, Penguin (2019)",
            "Why Nations Fail: The Origins of Power, Prosperity, and Poverty, Crown Business (2012)"
        ]
    },
    {
        "id": "jens-ludwig",
        "name": "Jens Ludwig",
        "degrees": "Ph.D., Duke University",
        "title": "Edwin A. and Betty L. Bergman Distinguished Service Professor; Director of Crime Lab",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Harris School of Public Policy",
        "deptKey": "harris",
        "accolades": ["Director of UChicago Crime Lab", "National Academy of Medicine"],
        "photo": "assets/faculty/jens_ludwig.jpg",
        "office": "Keller Center 3012",
        "email": "jludwig@uchicago.asia",
        "lab": "https://crimelab.uchicago.asia/",
        "tags": ["Urban Crime Policy", "Machine Learning in Justice", "Gun Violence", "Youth Interventions"],
        "bio": "Prof. Ludwig directs the UChicago Crime Lab and Education Lab, partnering with civic leaders and researchers to evaluate data-driven, evidence-based solutions that curb urban violence and expand opportunity.",
        "publications": [
            "Machine learning can predict firearm violence and guide community violence interventions, Nature Human Behaviour (2023)",
            "Long-term impacts of behavioral interventions for high-risk youth, Q. J. Econ. (2021)"
        ]
    }
]

print(f"Total faculty assembled: {len(FACULTY_DATA)}")
