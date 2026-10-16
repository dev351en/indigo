#!/usr/bin/env python3
"""
Complete Faculty Directory Generator for UChicago Replica.
Organizes 80+ prominent UChicago professors across all 6 academic domains:
1. Physical Sciences Division (PSD)
2. Biological Sciences Division & UChicago Medicine (BSD)
3. Social Sciences Division (SSD)
4. Humanities Division
5. Pritzker School of Molecular Engineering (PME)
6. Professional Schools (Booth, Law, Harris)
"""

import json
import os
import re

import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from generate_faculty_directory import FACULTY_DATA as BASE_FACULTY

# Add the 28 faculty who have real photos in assets/faculty
ADDITIONAL_PSD_PME_BSD = [
    {
        "id": "andrew-ferguson",
        "name": "Andrew L. Ferguson",
        "degrees": "Ph.D., Princeton University",
        "title": "Professor of Molecular Engineering & Vice Dean of Equity, Diversity, and Inclusion",
        "domain": "pme",
        "domainLabel": "Molecular Engineering (PME)",
        "department": "Pritzker School of Molecular Engineering & Chemistry",
        "deptKey": "pme",
        "accolades": ["Vice Dean of PME", "Camille Dreyfus Teacher-Scholar", "AI for Science Pioneer"],
        "photo": "assets/faculty/andrew_ferguson.jpg",
        "office": "Eckhardt Research Center 214",
        "email": "fergu@uchicago.asia",
        "lab": "https://ferguson.pme.uchicago.asia/",
        "tags": ["Machine Learning", "Molecular Simulation", "Antiviral Peptides", "Generative AI"],
        "bio": "Prof. Ferguson combines molecular simulation, statistical mechanics, and machine learning to design self-assembling materials and engineer biological polymers. His group develops generative AI platforms for de novo antiviral therapeutic design.",
        "publications": [
            "Active learning and generative models for peptide sequence optimization, Nat. Mach. Intell. (2023)",
            "Nonlinear manifold learning for molecular kinetics and free energy landscapes, Chem. Sci. (2022)"
        ]
    },
    {
        "id": "benoit-roux",
        "name": "Benoît Roux",
        "degrees": "Ph.D., Harvard University",
        "title": "Amgen Professor of Biochemistry and Molecular Biology & Professor of Chemistry",
        "domain": "bsd",
        "domainLabel": "Biological Sciences Division",
        "department": "Department of Biochemistry & Molecular Biology",
        "deptKey": "biochem",
        "accolades": ["Biophysical Society Fellow", "NAS Member", "National Institutes of Health MERIT Award"],
        "photo": "assets/faculty/beno_t_roux.jpg",
        "office": "Gordon Center for Integrative Science W242",
        "email": "roux@uchicago.asia",
        "lab": "https://thallium.bsd.uchicago.asia/RouxLab/",
        "tags": ["Ion Channels", "Molecular Dynamics", "Free Energy Perturbation", "Membrane Biophysics"],
        "bio": "Prof. Roux uses theoretical and computational methods to understand the microscopic workings of biological macromolecular machines. His lab models ion selectivity and voltage-gating in potassium and sodium channels.",
        "publications": [
            "Microscopic mechanism of voltage-dependent gating in potassium channels, Nature (2023)",
            "Free energy calculations for biomolecular systems: In pursuit of accuracy, Chem. Rev. (2022)"
        ]
    },
    {
        "id": "daniel-laorenza",
        "name": "Daniel Laorenza",
        "degrees": "Ph.D., Massachusetts Institute of Technology",
        "title": "Assistant Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["NIH Postdoctoral Fellow", "Inorganic Materials Innovator"],
        "photo": "assets/faculty/daniel_laorenza.png",
        "office": "Searle Chemistry Laboratory 122",
        "email": "dlaorenza@uchicago.asia",
        "lab": "https://chemistry.uchicago.asia/faculty/daniel-laorenza",
        "tags": ["Inorganic Synthesis", "Coordination Chemistry", "Electronic Materials", "Spin Dynamics"],
        "bio": "Prof. Laorenza develops precision synthetic synthetic routes to transition metal clusters, metal-radical networks, and solid-state materials exhibiting novel magnetic, optical, and quantum coherent phenomena.",
        "publications": [
            "Strong magnetic coupling in mixed-valence transition metal clusters, JACS (2024)",
            "Synthetically tunable spin-lattice relaxation in molecular quantum bits, Inorg. Chem. (2023)"
        ]
    },
    {
        "id": "david-mazziotti",
        "name": "David A. Mazziotti",
        "degrees": "Ph.D., Harvard University",
        "title": "Professor of Chemistry & The James Franck Institute",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["APS Fellow", "ACS Fellow", "International Academy of Quantum Molecular Science"],
        "photo": "assets/faculty/david_mazziotti.jpg",
        "office": "Searle Chemistry Laboratory 330",
        "email": "damazz@uchicago.asia",
        "lab": "https://mazziottigroup.uchicago.asia/",
        "tags": ["Reduced Density Matrices", "Quantum Computing", "Electronic Structure", "Strong Correlation"],
        "bio": "Prof. Mazziotti's group develops reduced-density-matrix (RDM) mechanics to calculate the electronic structure of strongly correlated molecules without wavefunctions, implementing these algorithms on noisy intermediate-scale quantum (NISQ) computers.",
        "publications": [
            "Quantum computational calculation of molecular excited states via reduced density matrices, Phys. Rev. Lett. (2023)",
            "Exact contracted Schrodinger equation for strongly correlated electrons, J. Chem. Phys. (2022)"
        ]
    },
    {
        "id": "dipti-jasrasaria",
        "name": "Dipti Jasrasaria",
        "degrees": "Ph.D., UC Berkeley",
        "title": "Assistant Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["Arnold O. Beckman Postdoctoral Fellow", "Physical Chemistry Scholar"],
        "photo": "assets/faculty/dipti_jasrasaria.jpg",
        "office": "Searle Chemistry Laboratory 236",
        "email": "djasrasaria@uchicago.asia",
        "lab": "https://jasrasarialab.uchicago.asia/",
        "tags": ["Nonequilibrium Quantum Dynamics", "Energy Transport", "Open Quantum Systems", "Photophysics"],
        "bio": "The Jasrasaria group develops theoretical and computational tools to understand how quantum mechanical effects dictate energy and charge transport in complex, nanoscale environments like light-harvesting complexes and polaritonic cavities.",
        "publications": [
            "Vibrational coherence and non-adiabatic transport in photosynthetic light harvesting, J. Phys. Chem. Lett. (2024)",
            "Generalized quantum master equations for condensed-phase excitonic systems, Chem. Sci. (2023)"
        ]
    },
    {
        "id": "elena-shevchenko",
        "name": "Elena V. Shevchenko",
        "degrees": "Ph.D., University of Hamburg",
        "title": "Professor of Chemistry & Senior Scientist, Argonne National Laboratory",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & Argonne",
        "deptKey": "chemistry",
        "accolades": ["Presidential Early Career Award (PECASE)", "Top Innovators Under 35 (TR35)"],
        "photo": "assets/faculty/elena_shevchenko.jpg",
        "office": "Searle Chemistry Laboratory 142",
        "email": "eshevchenko@uchicago.asia",
        "lab": "https://shevchenkogroup.uchicago.asia/",
        "tags": ["Nanoparticle Superlattices", "Self-Assembly", "Correlated Magnetism", "Catalytic Metamaterials"],
        "bio": "Prof. Shevchenko studies self-assembly of colloidal nanoparticles into binary and ternary superlattices, creating artificial solid-state materials with engineered optical, electronic, and magnetic cooperative properties.",
        "publications": [
            "Three-dimensional multi-component nanoparticle superlattices, Science (2023)",
            "Dynamic phase transitions in co-crystallizing magnetic nanoparticles, JACS (2021)"
        ]
    },
    {
        "id": "giulia-galli",
        "name": "Giulia Galli",
        "degrees": "Ph.D., International School for Advanced Studies (SISSA)",
        "title": "Liew Family Professor of Molecular Engineering and Chemistry",
        "domain": "pme",
        "domainLabel": "Molecular Engineering (PME)",
        "department": "PME & Department of Chemistry",
        "deptKey": "pme",
        "accolades": ["National Academy of Sciences", "American Academy of Arts and Sciences", "APS Aneesur Rahman Prize"],
        "photo": "assets/faculty/giulia_galli.png",
        "office": "Eckhardt Research Center 222",
        "email": "gagalli@uchicago.asia",
        "lab": "https://galligroup.uchicago.asia/",
        "tags": ["Quantum Information Science", "First-Principles Modeling", "Point Defects", "Water Under Pressure"],
        "bio": "Prof. Galli is an international leader in ab initio quantum simulations of matter, focusing on point defects in wide-bandgap semiconductors for quantum sensing and quantum computation, as well as electronic properties of renewable energy materials.",
        "publications": [
            "Spin defects in semiconductors for quantum technologies: Predictions from first principles, PRX Quantum (2023)",
            "Dielectric properties and electronic structure of liquid water under extreme pressures, PNAS (2022)"
        ]
    },
    {
        "id": "greg-engel",
        "name": "Greg Engel",
        "degrees": "Ph.D., Harvard University",
        "title": "Professor of Chemistry & Molecular Engineering; Director of Midwest Integrated Center for Quantum Materials",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & PME",
        "deptKey": "chemistry",
        "accolades": ["Director of MICCoM", "PECASE Recipient", "Searle Scholar", "ACS Pure Chemistry Award"],
        "photo": "assets/faculty/greg_engel.jpg",
        "office": "Gordon Center for Integrative Science W107",
        "email": "gsengel@uchicago.asia",
        "lab": "https://engellab.uchicago.asia/",
        "tags": ["Quantum Biology", "2D Electronic Spectroscopy", "Exciton Dynamics", "Photosynthetic Coherence"],
        "bio": "Prof. Engel pioneered 2D electronic spectroscopy experiments that uncovered long-lived electronic quantum coherence in photosynthetic complexes, advancing understanding of quantum transport in biological light-harvesting.",
        "publications": [
            "Quantum coherence in photosynthetic complexes under physiological conditions, Nature (2023)",
            "Ultrafast excitonic energy transfer pathways in artificial multi-chromophore arrays, JACS (2022)"
        ]
    },
    {
        "id": "guangbin-dong",
        "name": "Guangbin Dong",
        "degrees": "Ph.D., Stanford University",
        "title": "Weldon G. Brown Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["Elias J. Corey Award", "Sloan Research Fellow", "Blavatnik National Awards Finalist"],
        "photo": "assets/faculty/guangbin_dong.jpg",
        "office": "Searle Chemistry Laboratory 202",
        "email": "gbdong@uchicago.asia",
        "lab": "https://donggroup.uchicago.asia/",
        "tags": ["C-C Bond Activation", "Transition-Metal Catalysis", "Cascade Reactions", "Drug Discovery"],
        "bio": "Prof. Dong's group develops new catalytic paradigms for activating inert carbon-carbon and carbon-hydrogen bonds, creating catalytic transformations that streamline the synthesis of complex natural products and medicinal drugs.",
        "publications": [
            "Catalytic activation and cleavage of unstrained carbon-carbon bonds, Nature Chem. (2023)",
            "Palladium/norbornene cooperative catalysis for skeletal restructuring of ketones, Science (2021)"
        ]
    },
    {
        "id": "hannah-lant",
        "name": "Hannah M. Lant",
        "degrees": "Ph.D., Yale University",
        "title": "Assistant Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["DOE Early Career Awardee", "Arnold O. Beckman Fellow"],
        "photo": "assets/faculty/hannah_lant.png",
        "office": "Searle Chemistry Laboratory 324",
        "email": "hlant@uchicago.asia",
        "lab": "https://lantlab.uchicago.asia/",
        "tags": ["Metal-Organic Frameworks", "Photocatalysis", "Artificial Photosynthesis", "Porous Materials"],
        "bio": "The Lant Laboratory synthesizes hierarchical porous frameworks and metal-organic cages designed to stabilize catalytic intermediates for solar water splitting, carbon capture, and multi-electron redox transformations.",
        "publications": [
            "Spatial orchestration of multi-electron photocatalysts inside metal-organic frameworks, Chem. Sci. (2024)",
            "Operando X-ray spectroscopy of water oxidation centers in MOF thin films, JACS (2023)"
        ]
    },
    {
        "id": "hening-lin",
        "name": "Hening Lin",
        "degrees": "Ph.D., Columbia University",
        "title": "Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & Biochemistry",
        "deptKey": "chemistry",
        "accolades": ["HHMI Investigator Emeritus", "ACS Chemical Biology Lectureship"],
        "photo": "assets/faculty/hening_lin.jpg",
        "office": "Searle Chemistry Laboratory 212",
        "email": "heninglin@uchicago.asia",
        "lab": "https://linlab.uchicago.asia/",
        "tags": ["Post-Translational Modifications", "Sirtuins", "NAD+ Biology", "Chemical Epigenetics"],
        "bio": "Prof. Lin investigates sirtuins and novel post-translational protein acylations (malonylation, succinylation, glutarylation). His lab discovers regulatory mechanisms governing metabolism, innate immunity, and cancer survival.",
        "publications": [
            "Sirtuin deacylation regulates mitochondrial metabolic rewiring in tumor immunity, Nature (2023)",
            "Targeting metabolic enzymes with activity-based chemical probes, ACS Chem. Biol. (2022)"
        ]
    },
    {
        "id": "jie-zhou",
        "name": "Jie Zhou",
        "degrees": "Ph.D., Harvard University",
        "title": "Assistant Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["NIH Pathway to Independence Award", "Young Investigator Award"],
        "photo": "assets/faculty/jie_zhou.jpg",
        "office": "Searle Chemistry Laboratory 114",
        "email": "jiezhou@uchicago.asia",
        "lab": "https://zhougroup.uchicago.asia/",
        "tags": ["Spectroscopy", "Correlated Quantum Materials", "Ultrafast Optics", "Topological Insulators"],
        "bio": "Prof. Zhou's research utilizes ultrafast laser spectroscopy and terahertz near-field microscopy to capture nonequilibrium charge and spin dynamics in correlated electronic systems and topological insulators.",
        "publications": [
            "Terahertz near-field optical microscopy of phase transitions in correlated oxides, Nature Physics (2023)",
            "Coherent lattice polarons in layered 2D chalcogenides, Nano Lett. (2022)"
        ]
    },
    {
        "id": "john-anderson",
        "name": "John S. Anderson",
        "degrees": "Ph.D., California Institute of Technology",
        "title": "Associate Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["Presidential Early Career Award (PECASE)", "Sloan Research Fellow", "Packard Fellow"],
        "photo": "assets/faculty/john_anderson.jpg",
        "office": "Searle Chemistry Laboratory 104",
        "email": "jsanderson@uchicago.asia",
        "lab": "https://andersonlab.uchicago.asia/",
        "tags": ["Inorganic Chemistry", "Radical Ligands", "Conductive MOFs", "Small Molecule Activation"],
        "bio": "The Anderson Laboratory designs reactive transition metal complexes and conductive metal-organic frameworks featuring non-innocent radical ligands capable of facilitating multi-electron bond-forming reactions.",
        "publications": [
            "High electrical conductivity and metallic behavior in 2D sulfur-linked MOFs, Science (2023)",
            "Dinitrogen activation and functionalization by low-valent iron-chalcogenide clusters, JACS (2021)"
        ]
    },
    {
        "id": "joseph-piccirilli",
        "name": "Joseph A. Piccirilli",
        "degrees": "Ph.D., Harvard University",
        "title": "Professor of Biochemistry and Molecular Biology & Chemistry",
        "domain": "bsd",
        "domainLabel": "Biological Sciences Division",
        "department": "Department of Biochemistry & Molecular Biology",
        "deptKey": "biochem",
        "accolades": ["National Academy of Sciences", "AAAS Fellow", "Searle Scholar"],
        "photo": "assets/faculty/joseph_piccirilli.jpg",
        "office": "Gordon Center for Integrative Science W228",
        "email": "jpicciri@uchicago.asia",
        "lab": "https://piccirillilab.bsd.uchicago.asia/",
        "tags": ["Ribozymes", "RNA Splicing", "Catalytic RNA", "Structural Biology"],
        "bio": "Prof. Piccirilli is an authority on the chemical mechanism of RNA catalysis. His lab investigates catalytic ribozymes, the spliceosome core, and retrotransposons using biochemical, crystallographic, and cryo-EM methodologies.",
        "publications": [
            "Structural basis for RNA cleavage by the group II intron ribozyme, Nature Struct. Mol. Biol. (2023)",
            "Mechanism of branch-site selection in eukaryotic pre-mRNA splicing, Science (2021)"
        ]
    },
    {
        "id": "ka-yee-lee",
        "name": "Ka Yee C. Lee",
        "degrees": "Ph.D., Harvard University",
        "title": "David Lee Shillinglaw Distinguished Service Professor; Executive Vice President for Strategic Initiatives",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & The College",
        "deptKey": "chemistry",
        "accolades": ["Former Provost of UChicago", "APS Fellow", "Biophysical Society Fellow"],
        "photo": "assets/faculty/ka_yee_lee.png",
        "office": "Levi Hall 504 / Searle 318",
        "email": "kayeelee@uchicago.asia",
        "lab": "https://leelab.uchicago.asia/",
        "tags": ["Lipid Membranes", "Lung Surfactants", "Amyloid Fibrils", "Biophysical Interfaces"],
        "bio": "Prof. Lee's research focuses on the behavior of complex thin films and biomembranes, elucidating how lung surfactants operate at the alveolar interface and the molecular mechanisms of membrane disruption by amyloid peptides.",
        "publications": [
            "Thermodynamic and structural consequences of cholesterol on lung surfactant lipid films, Biophys. J. (2023)",
            "Molecular mechanisms of lipid extraction by antimicrobial peptides, Langmuir (2021)"
        ]
    },
    {
        "id": "michael-hopkins",
        "name": "Michael D. Hopkins",
        "degrees": "Ph.D., California Institute of Technology",
        "title": "Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["Camille Dreyfus Teacher-Scholar", "Alfred P. Sloan Research Fellow"],
        "photo": "assets/faculty/michael_hopkins.jpg",
        "office": "Searle Chemistry Laboratory 220",
        "email": "mhopkins@uchicago.asia",
        "lab": "https://chemistry.uchicago.asia/faculty/michael-hopkins",
        "tags": ["Inorganic Photochemistry", "Electronic Conjugation", "Metal-Alkylidyne Complexes", "Optoelectronics"],
        "bio": "Prof. Hopkins explores the electronic structure, bonding, and photophysics of conjugated metal-organic compounds. His laboratory designs tungsten and molybdenum alkylidyne complexes for nonlinear optical applications.",
        "publications": [
            "Electronic delocalization in pi-conjugated metal-alkylidyne oligomers, Inorg. Chem. (2023)",
            "Optical nonlinearities in transition metal coordination polymers, Chem. Mater. (2021)"
        ]
    },
    {
        "id": "norbert-scherer",
        "name": "Norbert F. Scherer",
        "degrees": "Ph.D., California Institute of Technology",
        "title": "Professor of Chemistry & The James Franck Institute",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & Physics",
        "deptKey": "chemistry",
        "accolades": ["APS Fellow", "Optical Society of America Fellow", "Guggenheim Fellow"],
        "photo": "assets/faculty/norbert_scherer.jpg",
        "office": "GCIS E201",
        "email": "nfschere@uchicago.asia",
        "lab": "https://schererlab.uchicago.asia/",
        "tags": ["Optical Tweezers", "Nanophotonics", "Matter-Wave Dynamics", "Single-Molecule Tracking"],
        "bio": "Prof. Scherer studies optical matter and nanoparticle assembly governed by light forces. His group creates dynamic optical lattices using electrodynamic interactions to direct matter at the nanoscale.",
        "publications": [
            "Observation of non-reciprocal optical forces in structured light fields, Nature Photonics (2023)",
            "Dynamic assembly and collective oscillations of optical matter arrays, Optica (2021)"
        ]
    },
    {
        "id": "philippe-guyot-sionnest",
        "name": "Philippe Guyot-Sionnest",
        "degrees": "Ph.D., UC Berkeley",
        "title": "Professor of Chemistry and Physics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & Physics",
        "deptKey": "chemistry",
        "accolades": ["APS Fellow", "AAAS Fellow", "Alexander von Humboldt Award"],
        "photo": "assets/faculty/philippe_guyot_sionnest.jpg",
        "office": "GCIS E105",
        "email": "pgs@uchicago.asia",
        "lab": "https://guyot-sionnest.uchicago.asia/",
        "tags": ["Colloidal Quantum Dots", "Infrared Optics", "Plasmonics", "Optoelectronic Devices"],
        "bio": "Prof. Guyot-Sionnest is a pioneer in colloidal quantum dots and infrared optoelectronics. His group created the first colloidal quantum dot infrared lasers and detectors operating across mid- and far-infrared wavelengths.",
        "publications": [
            "Intraband infrared photoluminescence and lasing in colloidal quantum dots, Nature Photonics (2023)",
            "Hot electron relaxation dynamics in n-doped semiconductor nanocrystals, Nano Lett. (2021)"
        ]
    },
    {
        "id": "raymond-moellering",
        "name": "Raymond E. Moellering",
        "degrees": "Ph.D., Harvard University",
        "title": "Associate Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & Cancer Research",
        "deptKey": "chemistry",
        "accolades": ["NIH Director's New Innovator Award", "Pew Biomedical Scholar", "V Foundation Scholar"],
        "photo": "assets/faculty/raymond_moellering.png",
        "office": "Searle Chemistry Laboratory 216",
        "email": "rmoellering@uchicago.asia",
        "lab": "https://moelleringlab.uchicago.asia/",
        "tags": ["Chemical Proteomics", "Metabolism", "Targeted Degradation", "Cancer Signaling"],
        "bio": "Prof. Moellering's group develops chemoproteomic technologies to map reactive metabolite-protein modifications, discovering allosteric regulation sites and therapeutic vulnerabilities in aggressive human cancers.",
        "publications": [
            "Chemoproteomic profiling reveals functional metabolic stress sensors in breast cancer, Cell Chem. Biol. (2023)",
            "Targeting oncoprotein dimers with stapled peptide probes, PNAS (2021)"
        ]
    },
    {
        "id": "sarah-king",
        "name": "Sarah B. King",
        "degrees": "Ph.D., UC Berkeley",
        "title": "Assistant Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["DOE Early Career Award", "Beckman Young Investigator", "Air Force Young Investigator"],
        "photo": "assets/faculty/sarah_king.png",
        "office": "Searle Chemistry Laboratory 126",
        "email": "sbking@uchicago.asia",
        "lab": "https://kinglab.uchicago.asia/",
        "tags": ["Photoemission Microscopy", "Interfacial Electronic Structure", "2D Heterostructures", "Ultrafast"],
        "bio": "Prof. King investigates electronic dynamics at nanoscale interfaces using time-resolved photoemission electron microscopy (TR-PEEM), tracking charge separation and exciton diffusion in next-generation photovoltaics.",
        "publications": [
            "Direct visualization of spatial exciton diffusion in MoS2/WS2 heterobilayers, Nat. Commun. (2023)",
            "Ultrafast charge injection dynamics at organic-semiconductor junctions, J. Phys. Chem. C (2022)"
        ]
    },
    {
        "id": "scott-snyder",
        "name": "Scott A. Snyder",
        "degrees": "Ph.D., The Scripps Research Institute",
        "title": "Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["Arthur C. Cope Scholar", "Amgen Young Investigator", "Bristol-Myers Squibb Award"],
        "photo": "assets/faculty/scott_snyder.jpg",
        "office": "Searle Chemistry Laboratory 204",
        "email": "snydersa@uchicago.asia",
        "lab": "https://snydergroup.uchicago.asia/",
        "tags": ["Total Synthesis", "Natural Products", "Halogenation Reagents", "Medicinal Chemistry"],
        "bio": "Prof. Snyder designs concise, general synthetic strategies to construct complex bioactive natural products, inventing novel reagents for selective halogenation and polycyclic architectures.",
        "publications": [
            "Total synthesis of complex halogenated marine alkaloids via biomimetic cascades, Nature Chem. (2023)",
            "Programmable reagent platforms for stereoselective halofunctionalization, JACS (2021)"
        ]
    },
    {
        "id": "shaunna-mcleod",
        "name": "Shaunna M. McLeod",
        "degrees": "Ph.D., Harvard University",
        "title": "Assistant Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["NIH Postdoctoral Fellow", "Biological Chemistry Educator"],
        "photo": "assets/faculty/shaunna_mcleod.png",
        "office": "Searle Chemistry Laboratory 308",
        "email": "smcleod@uchicago.asia",
        "lab": "https://chemistry.uchicago.asia/faculty/shaunna-mcleod",
        "tags": ["Chemical Biology", "Enzyme Mechanisms", "Pathogen Defense", "Bacterial Cell Wall"],
        "bio": "Prof. McLeod's laboratory investigates bacterial enzymatic pathways involved in antibiotic resistance and cell wall biosynthesis, developing chemical inhibitors that restore antibiotic susceptibility.",
        "publications": [
            "Structural characterization of peptidoglycan transglycosylase inhibition, Biochemistry (2023)",
            "Mechanism of allosteric regulation in bacterial cell envelope enzymes, J. Biol. Chem. (2021)"
        ]
    },
    {
        "id": "steven-sibener",
        "name": "Steven J. Sibener",
        "degrees": "Ph.D., UC Berkeley",
        "title": "Carl William Eisendrath Distinguished Service Professor of Chemistry & The James Franck Institute",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & Physics",
        "deptKey": "chemistry",
        "accolades": ["Arthur W. Adamson Award", "APS Fellow", "AVS Fellow", "Director of JFI Emeritus"],
        "photo": "assets/faculty/steven_sibener.jpg",
        "office": "GCIS E205",
        "email": "s-sibener@uchicago.asia",
        "lab": "https://sibenergroup.uchicago.asia/",
        "tags": ["Surface Chemistry", "Molecular Beam Scattering", "Scanning Probe Microscopy", "Polymer Films"],
        "bio": "Prof. Sibener is a pioneer in surface and materials chemistry. His laboratory utilizes supersonic molecular beam scattering and variable-temperature scanning probe microscopy to study gas-surface reaction dynamics.",
        "publications": [
            "Direct visualization of atomic-scale corrosion and passivation on metal single crystals, Science (2023)",
            "Supersonic beam scattering investigations of energy transfer at gas-polymer interfaces, PNAS (2021)"
        ]
    },
    {
        "id": "stuart-rowan",
        "name": "Stuart J. Rowan",
        "degrees": "Ph.D., University of Glasgow",
        "title": "Barry L. MacLean Professor of Molecular Engineering and Chemistry",
        "domain": "pme",
        "domainLabel": "Molecular Engineering (PME)",
        "department": "PME & Department of Chemistry",
        "deptKey": "pme",
        "accolades": ["ACS Fellow", "RSC Fellow", "Editor-in-Chief of ACS Macro Letters"],
        "photo": "assets/faculty/stuart_rowan.jpg",
        "office": "Eckhardt Research Center 308",
        "email": "stuartrowan@uchicago.asia",
        "lab": "https://rowangroup.uchicago.asia/",
        "tags": ["Supramolecular Polymers", "Dynamic Covalent Chemistry", "Self-Healing Materials", "Cellulose Nanocrystals"],
        "bio": "Prof. Rowan develops stimuli-responsive supramolecular polymers, dynamic covalent networks (vitrimers), and bio-derived nanocomposites capable of autonomous healing, shape-memory transitions, and chemical recycling.",
        "publications": [
            "Circularly recyclable thermosets based on dynamic boronic ester networks, Nature Materials (2023)",
            "Mechanically adaptive nanocomposites inspired by sea cucumber dermis, Science (2021)"
        ]
    },
    {
        "id": "suri-vaikuntanathan",
        "name": "Suri Vaikuntanathan",
        "degrees": "Ph.D., University of Maryland",
        "title": "Professor of Chemistry & The James Franck Institute",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["Camille Dreyfus Teacher-Scholar", "Sloan Research Fellow", "ACS OpenEye Outstanding Junior Faculty"],
        "photo": "assets/faculty/suri_vaikuntanathan.jpg",
        "office": "GCIS E219",
        "email": "svaikunt@uchicago.asia",
        "lab": "https://vaikuntanathan-group.uchicago.asia/",
        "tags": ["Statistical Mechanics", "Active Matter", "Non-Equilibrium Physics", "Phase Transitions"],
        "bio": "Prof. Vaikuntanathan's group studies the statistical mechanics of driven systems, active matter, and self-assembly out of equilibrium, formulating principles of efficiency, dissipative work, and information harvesting.",
        "publications": [
            "Thermodynamic uncertainty relations in active multi-particle fluids, Phys. Rev. X (2023)",
            "Controlling self-assembly pathways using non-equilibrium dissipation, Nature Physics (2022)"
        ]
    },
    {
        "id": "viresh-rawal",
        "name": "Viresh H. Rawal",
        "degrees": "Ph.D., University of Pennsylvania",
        "title": "Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry",
        "deptKey": "chemistry",
        "accolades": ["Arthur C. Cope Scholar", "American Chemical Society Fellow", "Chair Emeritus of Chemistry"],
        "photo": "assets/faculty/viresh_rawal.jpg",
        "office": "Searle Chemistry Laboratory 208",
        "email": "vrawal@uchicago.asia",
        "lab": "https://rawalgroup.uchicago.asia/",
        "tags": ["Asymmetric Catalysis", "Hydrogen Bonding Catalysts", "Squaramides", "Complex Natural Products"],
        "bio": "Prof. Rawal developed the widely used squaramide and TADDOL-based chiral hydrogen-bonding organocatalysts, pioneering stereoselective cycloadditions and asymmetric methods for pharmaceutical synthesis.",
        "publications": [
            "Enantioselective organocatalysis via dual hydrogen-bond donors, Chem. Rev. (2023)",
            "Total synthesis of complex indole alkaloids via catalytic asymmetric cycloadditions, JACS (2021)"
        ]
    },
    {
        "id": "weixin-tang",
        "name": "Weixin Tang",
        "degrees": "Ph.D., University of Illinois at Urbana-Champaign",
        "title": "Assistant Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & Biochemistry",
        "deptKey": "chemistry",
        "accolades": ["NIH Director's New Innovator Award", "Searle Scholar", "Kavli Fellow"],
        "photo": "assets/faculty/weixin_tang.jpg",
        "office": "Searle Chemistry Laboratory 336",
        "email": "weixintang@uchicago.asia",
        "lab": "https://tanglab.uchicago.asia/",
        "tags": ["Genome Editing", "Directed Evolution", "Base Editors", "Enzyme Engineering"],
        "bio": "Prof. Tang creates precision molecular recording and genome-editing technologies. Her laboratory develops continuous directed evolution platforms to engineer next-generation base editors and prime editors.",
        "publications": [
            "Continuous directed evolution of precision base editors in mammalian cells, Nature Biotech. (2023)",
            "Engineered DNA polymerases for cellular event recording, Nature Chemical Biology (2021)"
        ]
    },
    {
        "id": "wenbin-lin",
        "name": "Wenbin Lin",
        "degrees": "Ph.D., University of Illinois at Urbana-Champaign",
        "title": "James Franck Professor of Chemistry",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Chemistry & Radiation Oncology",
        "deptKey": "chemistry",
        "accolades": ["Highly Cited Researcher (Top 0.1%)", "ACS Chemistry of Materials Award", "AAAS Fellow"],
        "photo": "assets/faculty/wenbin_lin.jpg",
        "office": "Searle Chemistry Laboratory 102",
        "email": "wenbinlin@uchicago.asia",
        "lab": "https://linlab.uchicago.asia/",
        "tags": ["Nanoscale MOFs", "Cancer Nanomedicine", "Radiotherapy Sensitizers", "Solar Fuels"],
        "bio": "Prof. Lin pioneered nanoscale metal-organic frameworks (nMOFs) and nanoscale coordination polymers (NCPs) for clinical cancer immunotherapy, radio-sensitization, and solar fuel photocatalysis.",
        "publications": [
            "Nanoscale metal-organic frameworks for enhanced checkpoint blockade immunotherapy, Nature Biomed. Eng. (2023)",
            "Single-site catalysts in metal-organic frameworks for artificial photosynthesis, Chem. Rev. (2022)"
        ]
    }
]

# Merge into unified list of 80 faculty
ALL_FACULTY = BASE_FACULTY + ADDITIONAL_PSD_PME_BSD

print(f"Total faculty merged: {len(ALL_FACULTY)}")

# Check domains
from collections import Counter
counts = Counter(f["domain"] for f in ALL_FACULTY)
print("Breakdown by domain:", counts)

def generate_faculty_html(is_subpage=False):
    asset_prefix = "../" if is_subpage else ""
    root_link = "../index.html" if is_subpage else "index.html"
    portal_link = "../portal.html" if is_subpage else "portal.html"
    faculty_link = "faculty.html" if is_subpage else "faculty.html"
    pages_prefix = "" if is_subpage else "pages/"

    # JSON data encoded for client-side instant filtering and search
    faculty_json = json.dumps(ALL_FACULTY)

    # Domain metadata
    domains = [
        {"key": "all", "name": "All Domains", "count": len(ALL_FACULTY)},
        {"key": "psd", "name": "Physical Sciences (PSD)", "count": counts["psd"]},
        {"key": "bsd", "name": "Biological Sciences & Medicine (BSD)", "count": counts["bsd"]},
        {"key": "ssd", "name": "Social Sciences (SSD)", "count": counts["ssd"]},
        {"key": "humanities", "name": "Humanities Division", "count": counts["humanities"]},
        {"key": "pme", "name": "Molecular Engineering (PME)", "count": counts["pme"]},
        {"key": "professional", "name": "Professional Schools (Booth, Law, Harris)", "count": counts["professional"]}
    ]

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Faculty Directory | The University of Chicago</title>
  <meta name="description" content="Explore distinguished faculty, Nobel laureates, endowed chairs, and research scholars across all six academic domains and divisions at the University of Chicago.">
  <meta property="og:title" content="Faculty Directory | The University of Chicago">
  <meta property="og:description" content="Systematic directory of faculty and scholars at the University of Chicago.">
  <meta property="og:image" content="{asset_prefix}assets/faculty/chuan_he.jpg">

  <!-- Core Fonts & Stylesheets -->
  <link rel="preload" href="{asset_prefix}webfonts/fa-solid-900.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{asset_prefix}css/fontawesome.min.css">
  <link rel="stylesheet" href="{asset_prefix}fonts/UChicagoSansSerif.css">
  <link rel="stylesheet" href="{asset_prefix}fonts/UChicagoSerif.css">
  <link rel="stylesheet" href="{asset_prefix}css/replica_1to1_enhancements.css">
  <link rel="stylesheet" href="{asset_prefix}css/all_components.bundle.css">

  <style>
    :root {{
      --uchicago-maroon: #800000;
      --uchicago-maroon-dark: #660000;
      --uchicago-charcoal: #222222;
      --uchicago-light-grey: #f4f4f4;
      --uchicago-border: #e2e2e2;
    }}

    body {{
      font-family: 'UChicagoSansSerif-Regular', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      color: #333333;
      background: #fafafa;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }}

    /* Hero Banner */
    .faculty-hero-banner {{
      background: linear-gradient(135deg, #111111 0%, #2b0000 50%, #4a0000 100%);
      color: #ffffff;
      padding: 56px 24px 44px;
      position: relative;
      overflow: hidden;
      border-bottom: 4px solid var(--uchicago-maroon);
    }}
    .faculty-hero-banner::after {{
      content: '';
      position: absolute;
      right: -40px;
      bottom: -60px;
      width: 380px;
      height: 380px;
      background-image: url('{asset_prefix}assets/phoenix.png');
      background-size: contain;
      background-repeat: no-repeat;
      opacity: 0.12;
      pointer-events: none;
    }}
    .faculty-hero-content {{
      max-width: 1240px;
      margin: 0 auto;
      position: relative;
      z-index: 2;
    }}
    .faculty-hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.25);
      border-radius: 20px;
      padding: 4px 14px;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 1.2px;
      font-weight: 600;
      color: #ffd2d2;
      margin-bottom: 16px;
    }}
    .faculty-hero-title {{
      font-family: 'UChicagoSerif', Georgia, serif;
      font-size: 44px;
      line-height: 1.15;
      font-weight: 700;
      margin: 0 0 14px;
      color: #ffffff;
    }}
    .faculty-hero-sub {{
      font-size: 18px;
      line-height: 1.55;
      color: #dedede;
      max-width: 820px;
      margin: 0 0 28px;
    }}

    /* Stat Ribbon */
    .stat-ribbon {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 16px;
      max-width: 900px;
      margin-top: 24px;
      padding-top: 24px;
      border-top: 1px solid rgba(255, 255, 255, 0.16);
    }}
    .stat-item {{
      display: flex;
      flex-direction: column;
    }}
    .stat-number {{
      font-family: 'UChicagoSerif', Georgia, serif;
      font-size: 32px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1;
      margin-bottom: 4px;
    }}
    .stat-label {{
      font-size: 12px;
      color: #c7c7c7;
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }}

    /* Main Container */
    .faculty-directory-wrap {{
      max-width: 1240px;
      margin: 0 auto;
      padding: 36px 20px 80px;
    }}

    /* Sticky Filter Toolbar */
    .directory-toolbar {{
      background: #ffffff;
      border: 1px solid var(--uchicago-border);
      border-radius: 4px;
      padding: 20px 24px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
      margin-bottom: 28px;
      position: sticky;
      top: 0;
      z-index: 80;
    }}
    .toolbar-row-top {{
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 18px;
    }}
    .search-input-box {{
      flex: 1 1 340px;
      position: relative;
    }}
    .search-input-box i {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: #888888;
      font-size: 15px;
    }}
    .search-input-box input {{
      width: 100%;
      box-sizing: border-box;
      padding: 11px 14px 11px 40px;
      border: 1px solid #cccccc;
      border-radius: 4px;
      font-size: 15px;
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
      background: #fafafa;
    }}
    .search-input-box input:focus {{
      border-color: var(--uchicago-maroon);
      background: #ffffff;
      box-shadow: 0 0 0 3px rgba(128, 0, 0, 0.12);
    }}
    .filter-dropdowns {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .filter-select {{
      padding: 10px 14px;
      border: 1px solid #cccccc;
      border-radius: 4px;
      font-size: 14px;
      background: #ffffff;
      color: #333333;
      cursor: pointer;
      outline: none;
    }}
    .filter-select:focus {{
      border-color: var(--uchicago-maroon);
    }}

    /* Domain Tabs */
    .domain-tabs {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      border-top: 1px solid #eeeeee;
      padding-top: 16px;
    }}
    .domain-tab-btn {{
      background: #f0f0f0;
      border: none;
      border-radius: 20px;
      padding: 7px 16px;
      font-size: 13px;
      font-weight: 600;
      color: #444444;
      cursor: pointer;
      transition: all 0.18s ease;
      white-space: nowrap;
    }}
    .domain-tab-btn:hover {{
      background: #e4e4e4;
      color: #111111;
    }}
    .domain-tab-btn.is-active {{
      background: var(--uchicago-maroon);
      color: #ffffff;
      box-shadow: 0 2px 6px rgba(128, 0, 0, 0.25);
    }}

    /* Results Header */
    .results-meta-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 22px;
      font-size: 14px;
      color: #666666;
    }}
    .results-count {{
      font-weight: 700;
      color: #111111;
    }}
    .results-reset-btn {{
      background: none;
      border: none;
      color: var(--uchicago-maroon);
      font-weight: 600;
      font-size: 13px;
      cursor: pointer;
      display: none;
      text-decoration: underline;
    }}

    /* Faculty Grid */
    .faculty-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 24px;
    }}

    /* Faculty Card */
    .faculty-card {{
      background: #ffffff;
      border: 1px solid var(--uchicago-border);
      border-radius: 6px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
      transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
      position: relative;
    }}
    .faculty-card:hover {{
      transform: translateY(-3px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.09);
      border-color: #bbbbbb;
    }}
    .card-top-accent {{
      height: 4px;
      background: var(--uchicago-maroon);
      width: 100%;
    }}

    .faculty-card-header {{
      padding: 20px;
      display: flex;
      gap: 16px;
      align-items: flex-start;
      border-bottom: 1px solid #f0f0f0;
    }}
    .faculty-avatar-wrap {{
      width: 84px;
      height: 84px;
      min-width: 84px;
      border-radius: 50%;
      overflow: hidden;
      border: 2px solid #ffffff;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
      position: relative;
      background: #eee;
    }}
    .faculty-avatar-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
    .faculty-avatar-fallback {{
      width: 100%;
      height: 100%;
      background: linear-gradient(135deg, #800000 0%, #4a0000 100%);
      color: #ffffff;
      font-family: 'UChicagoSerif', Georgia, serif;
      font-weight: 700;
      font-size: 26px;
      display: flex;
      align-items: center;
      justify-content: center;
      text-transform: uppercase;
      letter-spacing: 1px;
    }}

    .faculty-card-info {{
      flex: 1;
      min-width: 0;
    }}
    .faculty-division-pill {{
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      color: var(--uchicago-maroon);
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-bottom: 4px;
    }}
    .faculty-card-name {{
      font-family: 'UChicagoSerif', Georgia, serif;
      font-size: 20px;
      font-weight: 700;
      color: #111111;
      margin: 0 0 4px;
      line-height: 1.25;
    }}
    .faculty-degrees {{
      font-size: 12px;
      color: #777777;
      margin-bottom: 6px;
    }}
    .faculty-card-title {{
      font-size: 13px;
      color: #444444;
      line-height: 1.4;
      font-weight: 500;
    }}

    /* Card Body */
    .faculty-card-body {{
      padding: 16px 20px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .faculty-accolades-box {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 12px;
    }}
    .accolade-tag {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 11px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 3px;
      background: #fdf2f2;
      color: #800000;
      border: 1px solid #ffd8d8;
    }}
    .accolade-tag.nobel {{
      background: #fff8e6;
      color: #975a00;
      border-color: #ffe099;
      font-weight: 700;
    }}

    .faculty-tags-box {{
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
      margin-bottom: 16px;
    }}
    .research-pill {{
      font-size: 11px;
      background: #f2f4f8;
      color: #3b4d6b;
      padding: 3px 8px;
      border-radius: 3px;
    }}

    .faculty-meta-list {{
      font-size: 13px;
      color: #555555;
      margin-bottom: 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .meta-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .meta-row i {{
      color: #888888;
      width: 14px;
      text-align: center;
      font-size: 12px;
    }}
    .meta-row a {{
      color: var(--uchicago-maroon);
      text-decoration: none;
    }}
    .meta-row a:hover {{
      text-decoration: underline;
    }}

    /* Card Footer Action */
    .faculty-card-footer {{
      padding-top: 12px;
      border-top: 1px solid #f0f0f0;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .btn-view-profile {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #ffffff;
      border: 1px solid var(--uchicago-maroon);
      color: var(--uchicago-maroon);
      padding: 7px 14px;
      font-size: 13px;
      font-weight: 600;
      border-radius: 3px;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .btn-view-profile:hover {{
      background: var(--uchicago-maroon);
      color: #ffffff;
    }}
    .faculty-lab-link {{
      font-size: 12px;
      color: #666666;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .faculty-lab-link:hover {{
      color: var(--uchicago-maroon);
      text-decoration: underline;
    }}

    /* Detail Modal */
    .faculty-modal-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.65);
      z-index: 99999;
      align-items: center;
      justify-content: center;
      padding: 20px;
      backdrop-filter: blur(2px);
    }}
    .faculty-modal-overlay.is-active {{
      display: flex;
    }}
    .faculty-modal-box {{
      background: #ffffff;
      width: 100%;
      max-width: 760px;
      max-height: 88vh;
      overflow-y: auto;
      border-radius: 4px;
      border-top: 5px solid var(--uchicago-maroon);
      box-shadow: 0 14px 40px rgba(0, 0, 0, 0.25);
      position: relative;
      padding: 32px;
    }}
    .modal-close-btn {{
      position: absolute;
      top: 18px;
      right: 18px;
      background: none;
      border: none;
      font-size: 22px;
      color: #777777;
      cursor: pointer;
      line-height: 1;
    }}
    .modal-close-btn:hover {{
      color: #000000;
    }}
    .modal-header-section {{
      display: flex;
      gap: 20px;
      align-items: flex-start;
      margin-bottom: 24px;
      padding-bottom: 20px;
      border-bottom: 1px solid #eeeeee;
    }}
    .modal-avatar-wrap {{
      width: 110px;
      height: 110px;
      min-width: 110px;
      border-radius: 50%;
      overflow: hidden;
      border: 3px solid #ffffff;
      box-shadow: 0 3px 12px rgba(0,0,0,0.15);
      background: #eeeeee;
    }}
    .modal-avatar-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .modal-title-box h2 {{
      font-family: 'UChicagoSerif', Georgia, serif;
      font-size: 26px;
      margin: 0 0 6px;
      color: #111111;
    }}
    .modal-title-box p {{
      margin: 0 0 8px;
      color: #555555;
      font-size: 15px;
      line-height: 1.4;
    }}
    .modal-section-title {{
      font-family: 'UChicagoSerif', Georgia, serif;
      font-size: 18px;
      margin: 20px 0 10px;
      color: var(--uchicago-maroon);
      border-bottom: 1px solid #f0f0f0;
      padding-bottom: 6px;
    }}
    .modal-bio-text {{
      font-size: 15px;
      line-height: 1.65;
      color: #333333;
      margin-bottom: 18px;
    }}
    .modal-publications-list {{
      padding-left: 20px;
      margin: 0 0 20px;
      color: #444444;
      font-size: 14px;
      line-height: 1.6;
    }}
    .modal-publications-list li {{
      margin-bottom: 8px;
    }}

    /* Mobile Responsive Adjustments */
    @media (max-width: 768px) {{
      .faculty-hero-title {{
        font-size: 32px;
      }}
      .faculty-hero-sub {{
        font-size: 16px;
      }}
      .stat-ribbon {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .directory-toolbar {{
        padding: 16px;
      }}
      .toolbar-row-top {{
        flex-direction: column;
        align-items: stretch;
      }}
      .faculty-grid {{
        grid-template-columns: 1fr;
      }}
      .faculty-modal-box {{
        padding: 20px;
      }}
      .modal-header-section {{
        flex-direction: column;
        align-items: center;
        text-align: center;
      }}
    }}
  </style>
</head>
<body>

  <!-- Root Header & BrandBar -->
  <header class="EduHeader_container__2uGdE" id="header" data-mobilenavisopen="false" data-scrolldown="false">
    <a href="#maincontent" class="EduHeader_skipLink__188b9">Skip to main content</a>
    <a target="_self" class="EduHeader_logoContainer__1rYiP" aria-label="Logo" href="{root_link}">
      <span class="linkText">
        <img alt="The University of Chicago Logo" class="EduHeader_desktopLogo__2qFkS" src="{asset_prefix}assets/logo-background.svg"/>
        <img alt="The University of Chicago Logo" class="EduHeader_mobileLogo__2-wip" src="{asset_prefix}assets/logo-background-mobile.svg"/>
      </span>
    </a>
    <button id="mobileTogBtn" class="EduHeader_mobileNavToggle__1rFw5" aria-label="Show main menu" aria-expanded="false"></button>
    
    <!-- Mobile Navigation Drawer -->
    <div class="EduHeader_headerNavigation__3Hyzr EduHeader_mobileOnly__p1dMY" data-nav-context="mobile">
      <nav class="EduNavigation_container__2jUpk" aria-label="Main">
        <div class="single-col-inner">
          <div class="EduNavigation_navContainer__3rU6H">
            <ul class="EduNavigation_navList__-DNEa EduNavigation_leftNav__1H8RA">
              <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}who-we-are.html"><span class="linkText">Who We Are</span></a></li>
              <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}academics.html"><span class="linkText">Academics</span></a></li>
              <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}research-and-scholarship.html"><span class="linkText">Research</span></a></li>
              <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}admissions.html"><span class="linkText">Admissions</span></a></li>
              <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{faculty_link}"><span class="linkText" style="color:#800000;font-weight:700;">Faculty Directory</span></a></li>
              <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{portal_link}"><span class="linkText">Application Portal</span></a></li>
            </ul>
          </div>
        </div>
      </nav>
    </div>

    <!-- Desktop BrandBar & Navigation -->
    <div class="EduHeader_headerNavigation__3Hyzr EduHeader_desktopOnly__2L_Sd" data-nav-context="desktop">
      <div class="EduBrandBar_container__5LPzZ" data-brandbar="true">
        <div class="single-col-inner">
          <div class="EduBrandBar_innerContainer__3uAha">
            <div class="EduBrandBar_navList__8fxdi">
              <ul class="EduBrandBar_linkContainer__GvNmq">
                <li class="EduBrandBar_linkListItem__YDMHQ uchicago-portal-item">
                  <a href="{portal_link}" class="EduBrandBar_brandBarLink__2sbcq portal-trigger-btn">
                    <span class="linkText">APPLICATION PORTAL</span>
                  </a>
                </li>
                <li class="EduBrandBar_linkListItem__YDMHQ">
                  <a href="https://news.uchicago.asia" class="EduBrandBar_brandBarLink__2sbcq" target="_blank" rel="noopener noreferrer"><span class="linkText">News</span></a>
                </li>
                <li class="EduBrandBar_linkListItem__YDMHQ">
                  <a href="https://events.uchicago.asia/" class="EduBrandBar_brandBarLink__2sbcq" target="_blank" rel="noopener noreferrer"><span class="linkText">Events</span></a>
                </li>
                <li class="EduBrandBar_linkListItem__YDMHQ">
                  <a href="{pages_prefix}careers.html" class="EduBrandBar_brandBarLink__2sbcq"><span class="linkText">Careers</span></a>
                </li>
                <li class="EduBrandBar_infoDropdownContainer__2FlvZ EduBrandBar_linkListItem__YDMHQ" id="info-menu-desktop" data-infodropdownisopen="false">
                  <button class="EduBrandBar_infoDropdownButton__23iFj" aria-expanded="false" tabindex="0">Info For</button>
                  <ul class="EduBrandBar_infoDropdownList__3G6o9">
                    <li class="EduBrandBar_infoDropdownListItem__3KUhM"><a href="{pages_prefix}students.html"><span class="linkText">Students</span></a></li>
                    <li class="EduBrandBar_infoDropdownListItem__3KUhM"><a href="{faculty_link}" style="font-weight:700;color:#800000;"><span class="linkText">Faculty Directory</span></a></li>
                    <li class="EduBrandBar_infoDropdownListItem__3KUhM"><a href="https://intranet.uchicago.asia/info-for-staff" target="_blank" rel="noopener noreferrer"><span class="linkText">Staff</span></a></li>
                    <li class="EduBrandBar_infoDropdownListItem__3KUhM"><a href="https://alumniandfriends.uchicago.asia/" target="_blank" rel="noopener noreferrer"><span class="linkText">Alumni</span></a></li>
                    <li class="EduBrandBar_infoDropdownListItem__3KUhM"><a href="https://college.uchicago.asia/about/parents" target="_blank" rel="noopener noreferrer"><span class="linkText">Parents</span></a></li>
                  </ul>
                </li>
              </ul>
            </div>
            <div class="EduBrandBar_navList__8fxdi">
              <ul class="EduBrandBar_linkContainer__GvNmq">
                <li class="EduBrandBar_linkListItem__YDMHQ"><a href="{pages_prefix}visit.html" class="EduBrandBar_brandBarLink__2sbcq"><span class="linkText">Visit</span></a></li>
                <li class="EduBrandBar_linkListItem__YDMHQ"><a href="{pages_prefix}contact-us.html" class="EduBrandBar_brandBarLink__2sbcq"><span class="linkText">Contact Us</span></a></li>
                <li class="EduBrandBar_linkListItem__YDMHQ"><a href="{faculty_link}" class="EduBrandBar_brandBarLink__2sbcq"><span class="linkText">Directory</span></a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Main Desktop Nav -->
      <nav class="EduNavigation_container__2jUpk" aria-label="Main">
        <div class="single-col-inner">
          <div class="EduNavigation_navContainer__3rU6H">
            <ul class="EduNavigation_navList__-DNEa EduNavigation_leftNav__1H8RA">
              <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}who-we-are.html"><span class="linkText">Who We Are</span></a></li>
              <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}academics.html"><span class="linkText">Academics</span></a></li>
              <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}research-and-scholarship.html"><span class="linkText">Research</span></a></li>
              <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}admissions.html"><span class="linkText">Admissions</span></a></li>
            </ul>
            <ul class="EduNavigation_navList__-DNEa EduNavigation_rightNav__367Qa">
              <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}life-at-uchicago.html"><span class="linkText">Life at UChicago</span></a></li>
              <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID EduNavigation_linkHighlight__iQb01" href="{pages_prefix}medicine.html"><span class="linkText">UChicago Medicine</span></a></li>
              <li class="EduNavigation_navListItem__2Qihw"><a href="{faculty_link}" class="EduNavigation_l1Link__1J9ID"><span class="linkText" style="border-bottom: 2px solid #800000; font-weight: 700;">Faculty</span></a></li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </header>

  <main id="maincontent">
    <!-- Hero Banner -->
    <section class="faculty-hero-banner">
      <div class="faculty-hero-content">
        <div class="faculty-hero-badge">
          <i class="fa fa-university"></i> Academic Divisions &amp; Faculty
        </div>
        <h1 class="faculty-hero-title">Faculty Directory</h1>
        <p class="faculty-hero-sub">
          The University of Chicago is home to an extraordinary community of scholars, researchers, and educators pioneering breakthroughs and shaping disciplines across the physical, biological, and social sciences, the humanities, molecular engineering, and professional schools.
        </p>

        <!-- Stat Ribbon -->
        <div class="stat-ribbon">
          <div class="stat-item">
            <span class="stat-number">99</span>
            <span class="stat-label">Nobel Laureates</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">55+</span>
            <span class="stat-label">National Academy Members</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">34</span>
            <span class="stat-label">MacArthur Fellows</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">6</span>
            <span class="stat-label">Academic Domains</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Faculty Directory App -->
    <div class="faculty-directory-wrap">
      
      <!-- Interactive Sticky Toolbar -->
      <div class="directory-toolbar">
        <div class="toolbar-row-top">
          <!-- Real-time Search Input -->
          <div class="search-input-box">
            <i class="fa fa-search"></i>
            <input type="text" id="facultySearchInput" placeholder="Search by professor name, research area, tag, or office..." autocomplete="off">
          </div>

          <!-- Secondary Filters -->
          <div class="filter-dropdowns">
            <select id="departmentSelect" class="filter-select" aria-label="Filter by department">
              <option value="all">All Departments</option>
              <option value="chemistry">Department of Chemistry</option>
              <option value="cs">Computer Science &amp; Data</option>
              <option value="physics">Department of Physics</option>
              <option value="biochem">Biochemistry &amp; Mol. Biology</option>
              <option value="medicine">Medicine &amp; Oncology</option>
              <option value="genetics">Human Genetics &amp; Organismal</option>
              <option value="economics">Department of Economics</option>
              <option value="polisci">Political Science</option>
              <option value="sociology">Sociology &amp; Social Thought</option>
              <option value="philosophy">Philosophy &amp; Ethics</option>
              <option value="arthistory">Art History &amp; English</option>
              <option value="pme">Molecular Engineering (PME)</option>
              <option value="booth">Booth School of Business</option>
              <option value="law">The Law School</option>
              <option value="harris">Harris School of Public Policy</option>
            </select>

            <select id="accoladeSelect" class="filter-select" aria-label="Filter by distinction">
              <option value="all">All Distinctions</option>
              <option value="nobel">Nobel Prize Laureates</option>
              <option value="national-academy">National Academy Members (NAS/NAE/NAM)</option>
              <option value="macarthur">MacArthur 'Genius' Fellows</option>
              <option value="chairs">Deans &amp; Department Chairs</option>
            </select>
          </div>
        </div>

        <!-- Domain Filter Tabs -->
        <div class="domain-tabs" id="domainTabsContainer">
          {''.join(f'<button class="domain-tab-btn {"is-active" if d["key"] == "all" else ""}" data-domain="{d["key"]}">{d["name"]} ({d["count"]})</button>' for d in domains)}
        </div>
      </div>

      <!-- Results Meta Bar -->
      <div class="results-meta-bar">
        <div>
          Showing <span class="results-count" id="resultsCount">{len(ALL_FACULTY)}</span> faculty members
          <span id="activeFilterDesc" style="color:#777; margin-left: 8px;"></span>
        </div>
        <button class="results-reset-btn" id="resetFiltersBtn">Reset All Filters</button>
      </div>

      <!-- Grid of Faculty Cards -->
      <div class="faculty-grid" id="facultyGrid">
        <!-- Rendered by client script -->
      </div>
    </div>
  </main>

  <!-- Detail Profile Modal -->
  <div class="faculty-modal-overlay" id="facultyModal">
    <div class="faculty-modal-box" id="facultyModalBox">
      <button class="modal-close-btn" id="modalCloseBtn" aria-label="Close profile modal">&times;</button>
      <div id="modalContent">
        <!-- Injected dynamically -->
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="Footer_container__2dL8M">
    <div class="Footer_innerContainer__1hWCN single-col-inner">
      <div class="Footer_mainContainer__3KTjC">
        <div class="Footer_logoContainer__2DO2w">
          <img alt="The University of Chicago" width="403" height="92" class="Footer_logo__1Xaa8" src="{asset_prefix}assets/footerlogo.jpg"/>
        </div>
        <div class="Footer_addressContainer__1mlCc">
          <small class="Footer_addressTitle__LIIg1">The University of Chicago</small>
          <div class="Footer_address__13lG5">
            <address>Edward H. Levi Hall<br>5801 S. Ellis Ave.<br>Chicago, IL 60637</address>
          </div>
        </div>
        <ul class="Footer_linksContainer__3gO0S">
          <li class="Footer_linkListItem__3BK1B"><a href="{portal_link}" class="Footer_link__1w-x1"><span class="linkText">Application Portal</span></a></li>
          <li class="Footer_linkListItem__3BK1B"><a href="{faculty_link}" class="Footer_link__1w-x1"><span class="linkText">Faculty Directory</span></a></li>
          <li class="Footer_linkListItem__3BK1B"><a href="{pages_prefix}careers.html" class="Footer_link__1w-x1"><span class="linkText">Job Opportunities</span></a></li>
          <li class="Footer_linkListItem__3BK1B"><a href="{pages_prefix}visit.html" class="Footer_link__1w-x1"><span class="linkText">Visit UChicago</span></a></li>
          <li class="Footer_linkListItem__3BK1B"><a href="{pages_prefix}contact-us.html" class="Footer_link__1w-x1"><span class="linkText">Contact Us</span></a></li>
        </ul>
      </div>
      <div class="Footer_copyrightContainer__1pCJF">
        <small class="Footer_copyright__2jV9M">&copy; 2026 The University of Chicago. All rights reserved.</small>
      </div>
    </div>
  </footer>

  <!-- Faculty Interactive Runtime -->
  <script>
    (function () {{
      const FACULTY_DATA = {faculty_json};
      const assetPrefix = "{asset_prefix}";

      const gridEl = document.getElementById("facultyGrid");
      const searchInput = document.getElementById("facultySearchInput");
      const deptSelect = document.getElementById("departmentSelect");
      const accoladeSelect = document.getElementById("accoladeSelect");
      const domainTabsContainer = document.getElementById("domainTabsContainer");
      const countEl = document.getElementById("resultsCount");
      const resetBtn = document.getElementById("resetFiltersBtn");
      const activeFilterDesc = document.getElementById("activeFilterDesc");

      const modalOverlay = document.getElementById("facultyModal");
      const modalContent = document.getElementById("modalContent");
      const modalCloseBtn = document.getElementById("modalCloseBtn");

      let currentDomain = "all";
      let currentDept = "all";
      let currentAccolade = "all";
      let searchQuery = "";

      // Compute initials
      function getInitials(name) {{
        return name
          .split(" ")
          .filter(n => n && !n.includes("."))
          .map(n => n[0])
          .slice(0, 2)
          .join("");
      }}

      // Render Card HTML
      function renderCard(f) {{
        const initials = getInitials(f.name);
        const photoSrc = f.photo ? (assetPrefix + f.photo) : "";
        const isNobel = f.accolades && f.accolades.some(a => a.toLowerCase().includes("nobel"));

        const accoladesHtml = (f.accolades || []).slice(0, 3).map(acc => {{
          const isN = acc.toLowerCase().includes("nobel");
          return `<span class="accolade-tag ${{isN ? 'nobel' : ''}}">${{isN ? '<i class="fa fa-award"></i> ' : ''}}${{acc}}</span>`;
        }}).join("");

        const tagsHtml = (f.tags || []).slice(0, 4).map(t => 
          `<span class="research-pill">${{t}}</span>`
        ).join("");

        return `
          <div class="faculty-card" data-id="${{f.id}}" data-domain="${{f.domain}}" data-dept="${{f.deptKey}}">
            <div class="card-top-accent"></div>
            <div class="faculty-card-header">
              <div class="faculty-avatar-wrap">
                ${{photoSrc ? `
                  <img src="${{photoSrc}}" alt="${{f.name}}" loading="lazy" decoding="async" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                  <div class="faculty-avatar-fallback" style="display:none;">${{initials}}</div>
                ` : `
                  <div class="faculty-avatar-fallback">${{initials}}</div>
                `}}
              </div>
              <div class="faculty-card-info">
                <span class="faculty-division-pill">${{f.department}}</span>
                <h3 class="faculty-card-name">${{f.name}}</h3>
                <div class="faculty-degrees">${{f.degrees}}</div>
                <div class="faculty-card-title">${{f.title}}</div>
              </div>
            </div>

            <div class="faculty-card-body">
              ${{accoladesHtml ? `<div class="faculty-accolades-box">${{accoladesHtml}}</div>` : ''}}
              
              <div class="faculty-tags-box">${{tagsHtml}}</div>

              <div class="faculty-meta-list">
                ${{f.office ? `<div class="meta-row"><i class="fa fa-location-dot"></i> <span>${{f.office}}</span></div>` : ''}}
                ${{f.email ? `<div class="meta-row"><i class="fa fa-envelope"></i> <a href="mailto:${{f.email}}">${{f.email}}</a></div>` : ''}}
              </div>

              <div class="faculty-card-footer">
                <button class="btn-view-profile" onclick="window.openFacultyModal('${{f.id}}')">
                  <i class="fa fa-user-circle"></i> View Profile
                </button>
                ${{f.lab ? `
                  <a href="${{f.lab}}" target="_blank" rel="noopener noreferrer" class="faculty-lab-link">
                    Lab / Scholar Site <i class="fa fa-external-link-alt"></i>
                  </a>
                ` : ''}}
              </div>
            </div>
          </div>
        `;
      }}

      // Filter and Render
      function filterAndRender() {{
        const q = searchQuery.toLowerCase().trim();

        const filtered = FACULTY_DATA.filter(f => {{
          // Domain
          if (currentDomain !== "all" && f.domain !== currentDomain) return false;

          // Department
          if (currentDept !== "all" && f.deptKey !== currentDept) return false;

          // Distinction
          if (currentAccolade === "nobel") {{
            if (!f.accolades || !f.accolades.some(a => a.toLowerCase().includes("nobel"))) return false;
          }} else if (currentAccolade === "national-academy") {{
            if (!f.accolades || !f.accolades.some(a => a.toLowerCase().includes("national academy") || a.includes("NAS") || a.includes("NAE") || a.includes("NAM"))) return false;
          }} else if (currentAccolade === "macarthur") {{
            if (!f.accolades || !f.accolades.some(a => a.toLowerCase().includes("macarthur"))) return false;
          }} else if (currentAccolade === "chairs") {{
            if (!f.accolades || !f.accolades.some(a => a.toLowerCase().includes("chair") || a.toLowerCase().includes("dean") || a.toLowerCase().includes("president") || a.toLowerCase().includes("provost") || a.toLowerCase().includes("director"))) return false;
          }}

          // Text Search
          if (q) {{
            const searchHaystack = [
              f.name,
              f.title,
              f.department,
              f.domainLabel,
              f.degrees,
              f.office,
              f.bio,
              (f.tags || []).join(" "),
              (f.accolades || []).join(" "),
              (f.publications || []).join(" ")
            ].join(" ").toLowerCase();

            if (!searchHaystack.includes(q)) return false;
          }}

          return true;
        }});

        gridEl.innerHTML = filtered.map(renderCard).join("");
        countEl.textContent = filtered.length;

        // Reset button visibility
        const isFiltered = currentDomain !== "all" || currentDept !== "all" || currentAccolade !== "all" || q.length > 0;
        resetBtn.style.display = isFiltered ? "inline-block" : "none";

        // Active description
        let desc = [];
        if (currentDomain !== "all") desc.push(`Domain: ${{currentDomain.toUpperCase()}}`);
        if (currentDept !== "all") desc.push(`Dept: ${{currentDept}}`);
        if (currentAccolade !== "all") desc.push(`Filter: ${{currentAccolade}}`);
        if (q) desc.push(`Matching: "${{q}}"`);
        activeFilterDesc.textContent = desc.length ? `(${{desc.join(", ")}})` : "";
      }}

      // Event Listeners
      searchInput.addEventListener("input", function (e) {{
        searchQuery = e.target.value;
        filterAndRender();
      }});

      deptSelect.addEventListener("change", function (e) {{
        currentDept = e.target.value;
        filterAndRender();
      }});

      accoladeSelect.addEventListener("change", function (e) {{
        currentAccolade = e.target.value;
        filterAndRender();
      }});

      domainTabsContainer.addEventListener("click", function (e) {{
        const btn = e.target.closest(".domain-tab-btn");
        if (!btn) return;
        domainTabsContainer.querySelectorAll(".domain-tab-btn").forEach(b => b.classList.remove("is-active"));
        btn.classList.add("is-active");
        currentDomain = btn.getAttribute("data-domain");
        filterAndRender();
      }});

      resetBtn.addEventListener("click", function () {{
        currentDomain = "all";
        currentDept = "all";
        currentAccolade = "all";
        searchQuery = "";
        searchInput.value = "";
        deptSelect.value = "all";
        accoladeSelect.value = "all";
        domainTabsContainer.querySelectorAll(".domain-tab-btn").forEach(b => {{
          if (b.getAttribute("data-domain") === "all") b.classList.add("is-active");
          else b.classList.remove("is-active");
        }});
        filterAndRender();
      }});

      // Modal Handler
      window.openFacultyModal = function (id) {{
        const f = FACULTY_DATA.find(item => item.id === id);
        if (!f) return;

        const initials = getInitials(f.name);
        const photoSrc = f.photo ? (assetPrefix + f.photo) : "";

        const pubList = (f.publications || []).map(p => `<li>${{p}}</li>`).join("");
        const accoladesList = (f.accolades || []).map(a => `<span class="accolade-tag">${{a}}</span>`).join(" ");

        modalContent.innerHTML = `
          <div class="modal-header-section">
            <div class="modal-avatar-wrap">
              ${{photoSrc ? `
                <img src="${{photoSrc}}" alt="${{f.name}}" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                <div class="faculty-avatar-fallback" style="display:none; width:100%; height:100%; font-size:36px;">${{initials}}</div>
              ` : `
                <div class="faculty-avatar-fallback" style="width:100%; height:100%; font-size:36px;">${{initials}}</div>
              `}}
            </div>
            <div class="modal-title-box">
              <span class="faculty-division-pill">${{f.domainLabel}} &bull; ${{f.department}}</span>
              <h2>${{f.name}}</h2>
              <p><strong>${{f.title}}</strong></p>
              <p style="font-size:13px; color:#666;">${{f.degrees}}</p>
              <div style="margin-top: 10px;">${{accoladesList}}</div>
            </div>
          </div>

          <div class="modal-section-title">Biography &amp; Scholarly Contributions</div>
          <div class="modal-bio-text">${{f.bio}}</div>

          ${{f.tags && f.tags.length ? `
            <div class="modal-section-title">Research Areas &amp; Specializations</div>
            <div class="faculty-tags-box" style="margin-bottom:20px;">
              ${{f.tags.map(t => `<span class="research-pill" style="font-size:13px; padding:4px 10px;">${{t}}</span>`).join("")}}
            </div>
          ` : ''}}

          ${{pubList ? `
            <div class="modal-section-title">Selected Publications &amp; Works</div>
            <ul class="modal-publications-list">${{pubList}}</ul>
          ` : ''}}

          <div class="modal-section-title">Contact &amp; Campus Office</div>
          <div style="font-size:14px; line-height:1.7; color:#444;">
            ${{f.office ? `<div><strong>Campus Office:</strong> ${{f.office}}, The University of Chicago</div>` : ''}}
            ${{f.email ? `<div><strong>Email:</strong> <a href="mailto:${{f.email}}" style="color:#800000; font-weight:600;">${{f.email}}</a></div>` : ''}}
            ${{f.lab ? `<div style="margin-top:10px;"><a href="${{f.lab}}" target="_blank" rel="noopener noreferrer" style="color:#800000; text-decoration:underline; font-weight:600;">Visit Laboratory / Academic Directory Website &rarr;</a></div>` : ''}}
          </div>
        `;

        modalOverlay.classList.add("is-active");
      }};

      modalCloseBtn.addEventListener("click", function () {{
        modalOverlay.classList.remove("is-active");
      }});

      modalOverlay.addEventListener("click", function (e) {{
        if (e.target === modalOverlay) {{
          modalOverlay.classList.remove("is-active");
        }}
      }});

      document.addEventListener("keydown", function (e) {{
        if (e.key === "Escape" && modalOverlay.classList.contains("is-active")) {{
          modalOverlay.classList.remove("is-active");
        }}
      }});

      // Initial Render
      filterAndRender();

      // Mobile Menu Toggle Support
      var mobileToggle = document.getElementById("mobileTogBtn");
      var headerEl = document.getElementById("header");
      if (mobileToggle && headerEl) {{
        mobileToggle.addEventListener("click", function () {{
          var isOpen = headerEl.getAttribute("data-mobilenavisopen") === "true";
          headerEl.setAttribute("data-mobilenavisopen", !isOpen ? "true" : "false");
          mobileToggle.setAttribute("aria-expanded", !isOpen ? "true" : "false");
        }});
      }}
    }})();
  </script>
</body>
</html>
"""
    return html

# Generate root faculty.html
root_html = generate_faculty_html(is_subpage=False)
with open("site_1to1/faculty.html", "w", encoding="utf-8") as f:
    f.write(root_html)
print("Wrote site_1to1/faculty.html successfully!")

# Generate subpage pages/faculty.html
subpage_html = generate_faculty_html(is_subpage=True)
with open("site_1to1/pages/faculty.html", "w", encoding="utf-8") as f:
    f.write(subpage_html)
print("Wrote site_1to1/pages/faculty.html successfully!")

# Also write as static json for any client fetch if needed
with open("site_1to1/assets/faculty/faculty_directory.json", "w", encoding="utf-8") as f:
    json.dump(ALL_FACULTY, f, indent=2)
print("Wrote site_1to1/assets/faculty/faculty_directory.json successfully!")
