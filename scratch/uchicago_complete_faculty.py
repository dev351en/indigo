"""
Master Faculty Repository for The University of Chicago Replica.
Provides 140+ prominent UChicago professors across all departments and academic domains:
1. Physical Sciences Division (PSD): Computer Science, Economics, Physics, Mathematics, Statistics, Chemistry, Astronomy
2. Social Sciences Division (SSD): Economics, History, Political Science, Sociology, Anthropology
3. Biological Sciences Division (BSD) & Medicine: Biochemistry, Genetics, Neurobiology, Pritzker Medicine
4. Humanities Division: Philosophy, English, Art History, Music
5. Pritzker School of Molecular Engineering (PME)
6. Professional Schools: Booth School of Business, Law School, Harris School of Public Policy
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from generate_faculty_directory import FACULTY_DATA as BASE_FACULTY
from build_complete_faculty_directory import ADDITIONAL_PSD_PME_BSD

# Create dictionary keyed by ID to ensure uniqueness and allow enriching
FACULTY_MAP = {}

# 1. Ingest Base Faculty
for f in BASE_FACULTY:
    FACULTY_MAP[f["id"]] = f

# 2. Ingest Additional PSD/PME/BSD from build_complete_faculty_directory
for f in ADDITIONAL_PSD_PME_BSD:
    FACULTY_MAP[f["id"]] = f

# 3. Comprehensive Departmental Additions
NEW_FACULTY_ROSTER = [

    {
        'id': 'cathy-cohen',
        'name': 'Cathy J. Cohen',
        'degrees': 'Ph.D., University of Michigan',
        'title': 'David and Mary Winton Green Distinguished Service Professor of Political Science',
        'domain': 'ssd',
        'domainLabel': 'Social Sciences Division',
        'department': 'Department of Political Science',
        'deptKey': 'department-of-political-science',
        'accolades': ['David and Mary Winton Green Chair', 'American Academy of Arts and Sciences Member', 'Founder of GenForward Survey & Black Youth Project'],
        'photo': '',
        'office': 'Pick Hall 520',
        'email': 'cjcohen@uchicago.asia',
        'lab': 'https://genforwardsurvey.com/',
        'tags': ['Black Youth Project', 'GenForward', 'American Politics', 'Marginalization & Social Movements'],
        'bio': 'Prof. Cohen is the David and Mary Winton Green Distinguished Service Professor and creator of the Black Youth Project and GenForward Survey. Her research examines political participation, social justice, and systemic inequality in marginalized communities.',
        'publications': [
            'The Boundaries of Blackness: AIDS and the Breakdown of Black Politics, University of Chicago Press (1999)',
            'Democracy Remixed: Black Youth and the Future of American Politics, Oxford University Press (2010)'
        ]
    },
    {
        'id': 'jennifer-pitts',
        'name': 'Jennifer Pitts',
        'degrees': 'Ph.D., Harvard University',
        'title': 'Professor of Political Science and the Committee on Social Thought',
        'domain': 'ssd',
        'domainLabel': 'Social Sciences Division',
        'department': 'Department of Political Science',
        'deptKey': 'department-of-political-science',
        'accolades': ['Laing Prize Winner', 'Past Director of Neubauer Collegium Projects', 'International Political Theory Leader'],
        'photo': '',
        'office': 'Pick Hall 424',
        'email': 'jpitts@uchicago.asia',
        'lab': 'https://political-science.uchicago.asia/people/faculty/jennifer-pitts',
        'tags': ['Political Theory', 'International Law', 'Empire & Imperialism', 'History of Political Thought'],
        'bio': 'Prof. Pitts explores modern political and international thought, with particular attention to theories of empire, global justice, and the evolution of international law in British and French thought.',
        'publications': [
            'Boundaries of the International: Law and Empire, Harvard University Press (2018)',
            'A Turn to Empire: The Rise of Imperial Liberalism in Britain and France, Princeton University Press (2005)'
        ]
    },

   {   'accolades': [   'Department Chair',
                         "COPSS Presidents' Award (Honorable Mention)",
                         'Highly Cited Researcher',
                         'Royal Society Fellow Candidate'],
        'bio': 'Prof. Stephens is the Ralph W. Gerard Professor and Chair of the Department of Statistics. An '
               'international leader in computational biology, his statistical methods (such as STRUCTURE and '
               'fastStructure) have revolutionized the analysis of high-dimensional genetic variation and empirical '
               'Bayes shrinkage.',
        'degrees': 'D.Phil., University of Oxford',
        'department': 'Department of Statistics & Data Science',
        'deptKey': 'department-of-statistics',
        'domain': 'psd',
        'domainLabel': 'Physical Sciences Division',
        'email': 'mstephens@uchicago.asia',
        'id': 'matthew-stephens',
        'lab': 'https://stephenslab.uchicago.asia/',
        'name': 'Matthew Stephens',
        'office': 'Jones Laboratory 224',
        'photo': '',
        'publications': [   'Inference of population structure using multilocus genotype data, Genetics (2000)',
                            'A unified approach to false discovery rate estimation with empirical Bayes, Biostatistics '
                            '(2017)'],
        'tags': ['Statistical Genetics', 'Empirical Bayes', 'Markov Chain Monte Carlo', 'Genomic Variation'],
        'title': 'Ralph W. Gerard Professor of Statistics and Human Genetics & Department Chair'},
    {   'accolades': ['NSF CAREER Award', 'Google Faculty Research Award', 'Associate Editor of JASA'],
        'bio': 'Prof. Kolar investigates high-dimensional statistical inference, time-varying networks, and graphical '
               'models. His research establishes theoretical limits and algorithms for discovering complex relational '
               'structure in large, noisy genomic and econometric data.',
        'degrees': 'Ph.D., Carnegie Mellon University',
        'department': 'Department of Statistics & Data Science',
        'deptKey': 'department-of-statistics',
        'domain': 'psd',
        'domainLabel': 'Physical Sciences Division',
        'email': 'mkolar@uchicago.asia',
        'id': 'mladen-kolar',
        'lab': 'https://kolar.uchicago.asia/',
        'name': 'Mladen Kolar',
        'office': 'Jones Laboratory 218',
        'photo': '',
        'publications': [   'Estimating time-varying networks for high-dimensional data, J. R. Stat. Soc. B (2012)',
                            'Consistent estimation of dynamic graphical models, Ann. Stat. (2015)'],
        'tags': ['High-Dimensional Statistics', 'Graphical Models', 'Nonparametric Statistics', 'Machine Learning'],
        'title': 'Professor of Econometrics and Statistics'},
    {   'accolades': [   "COPSS Presidents' Award (2021)",
                         'Sloan Research Fellowship',
                         'Bernoulli Society New Researcher Award'],
        'bio': "Prof. Gao won the 2021 COPSS Presidents' Award, the highest international honor in statistics, for "
               'pioneering work in robust estimation, community detection in complex networks, and minimax rates of '
               'convergence for structured models.',
        'degrees': 'Ph.D., Yale University',
        'department': 'Department of Statistics & Data Science',
        'deptKey': 'department-of-statistics',
        'domain': 'psd',
        'domainLabel': 'Physical Sciences Division',
        'email': 'chaogao@uchicago.asia',
        'id': 'chao-gao',
        'lab': 'https://galton.uchicago.asia/~chaogao/',
        'name': 'Chao Gao',
        'office': 'Jones Laboratory 312',
        'photo': '',
        'publications': [   'Minimax optimal rates for network community detection, Ann. Stat. (2017)',
                            'Adversarial robust estimation with depth and median estimators, J. Am. Stat. Assoc. '
                            '(2020)'],
        'tags': ['Robust Statistics', 'Community Detection', 'Network Analysis', 'Minimax Estimation'],
        'title': 'Associate Professor of Statistics'},
    {   'accolades': [   'Director of Committee on Computational and Applied Mathematics (CAM)',
                         'AMS Fellow',
                         'SIAM Fellow'],
        'bio': 'Prof. Bal directs the Committee on Computational and Applied Mathematics (CAM). His research focuses '
               'on inverse problems in medical imaging, hybrid imaging modalities, and wave propagation through '
               'complex random media.',
        'degrees': 'Ph.D., University of Paris VI',
        'department': 'Department of Statistics & Data Science',
        'deptKey': 'department-of-statistics',
        'domain': 'psd',
        'domainLabel': 'Physical Sciences Division',
        'email': 'guillaumebal@uchicago.asia',
        'id': 'guillaume-bal',
        'lab': 'https://voices.uchicago.asia/guillaumebal/',
        'name': 'Guillaume Bal',
        'office': 'Jones Laboratory 320',
        'photo': '',
        'publications': [   'Hybrid inverse problems and quantitative photoacoustic tomography, Inverse Problems '
                            '(2012)',
                            'Topological protection of edge states in disordered media, Commun. Math. Phys. (2019)'],
        'tags': [   'Applied Mathematics',
                    'Inverse Problems',
                    'Wave Propagation in Random Media',
                    'Topological Insulators'],
        'title': 'Professor of Statistics and Mathematics & Director of CAM'},
    {   'accolades': [   'John W. Campbell Memorial Award',
                         'Celia & Joseph Burton Fellow',
                         'UChicago Faculty Award for Excellence in Graduate Teaching'],
        'bio': 'Prof. Palmer is an intellectual and cultural historian specializing in the European Renaissance, the '
               'history of censorship, and the recovery of classical philosophy. She also is an acclaimed speculative '
               'fiction author and directs international research on the censorship of radical thought.',
        'degrees': 'Ph.D., Harvard University',
        'department': 'Department of History',
        'deptKey': 'department-of-history',
        'domain': 'humanities',
        'domainLabel': 'Humanities Division',
        'email': 'adapalmer@uchicago.asia',
        'id': 'ada-palmer',
        'lab': 'https://history.uchicago.asia/people/ada-palmer',
        'name': 'Ada Palmer',
        'office': 'Social Science Research Building 223',
        'photo': '',
        'publications': [   'Reading Lucretius in the Renaissance, Harvard University Press (2014)',
                            'Terra Ignota: A History of Utopian Political Thought, Tor Books (2016-2021)'],
        'tags': ['Renaissance History', 'Censorship & Information Control', 'History of Ideas', 'Early Modern Science'],
        'title': 'Professor of Early Modern European History & The College'},
    {   'accolades': [   "MacArthur Fellow ('Genius Grant')",
                         'George Louis Beer Prize',
                         'American Academy of Arts and Sciences Member'],
        'bio': 'Prof. Zahra is a MacArthur Fellow and Homer J. Livingston Professor of History. Her transnational '
               'historical research explores the politics of migration, childhood, nationalism, and anti-globalist '
               'movements in modern Central and Eastern Europe.',
        'degrees': 'Ph.D., University of Michigan',
        'department': 'Department of History',
        'deptKey': 'department-of-history',
        'domain': 'humanities',
        'domainLabel': 'Humanities Division',
        'email': 'tzahra@uchicago.asia',
        'id': 'tara-zahra',
        'lab': 'https://neubauercollegium.uchicago.asia/',
        'name': 'Tara Zahra',
        'office': 'Social Science Research Building 214',
        'photo': '',
        'publications': [   'Against the World: Anti-Globalism and Decoupling in the Interwar Era, W. W. Norton (2023)',
                            'The Great Departure: Mass Migration from Eastern Europe and the Making of the Free World, '
                            'W. W. Norton (2016)'],
        'tags': ['MacArthur Fellow', 'East European History', 'Migration', 'Nationalism & Deglobalization'],
        'title': 'Homer J. Livingston Professor of East European History & Roman Family Director of Neubauer '
                 'Collegium'},
    {   'accolades': [   'Deputy Provost for International Affairs',
                         'Bernadotte E. Schmitt Professor',
                         'Guggenheim Fellow'],
        'bio': 'Prof. Bradley is Deputy Provost for International Affairs and Bernadotte E. Schmitt Distinguished '
               'Service Professor of History. His research focuses on the global history of human rights, the '
               'international impact of the Vietnam War, and twentieth-century postcolonial world orders.',
        'degrees': 'Ph.D., Harvard University',
        'department': 'Department of History',
        'deptKey': 'department-of-history',
        'domain': 'humanities',
        'domainLabel': 'Humanities Division',
        'email': 'mbradley@uchicago.asia',
        'id': 'mark-philip-bradley',
        'lab': 'https://history.uchicago.asia/people/mark-philip-bradley',
        'name': 'Mark Philip Bradley',
        'office': 'Social Science Research Building 208',
        'photo': '',
        'publications': [   'The World Reimagined: Americans and Human Rights in the Twentieth Century, Cambridge '
                            'University Press (2016)',
                            'Imagining Vietnam and America: The Making of Post-Colonial Vietnam, UNC Press (2000)'],
        'tags': ['International History', 'Human Rights', 'US-East Asian Relations', 'Post-Colonial Global Order'],
        'title': 'Bernadotte E. Schmitt Distinguished Service Professor of International History & Deputy Provost'},
    {   'accolades': [   'Evelyn Stefansson Nef Chair',
                         'American Philosophical Society Member',
                         'American Academy of Arts and Sciences',
                         'Mellon Distinguished Achievement Award'],
        'bio': 'Prof. Pippin is the Evelyn Stefansson Nef Distinguished Service Professor in the John U. Nef Committee '
               'on Social Thought and Department of Philosophy. He is internationally recognized as the foremost '
               'living interpreter of G.W.F. Hegel, German Idealism, and the philosophical dimensions of modernist '
               'cinema and literature.',
        'degrees': 'Ph.D., Pennsylvania State University',
        'department': 'Department of Philosophy',
        'deptKey': 'department-of-philosophy',
        'domain': 'humanities',
        'domainLabel': 'Humanities Division',
        'email': 'rbp1@uchicago.asia',
        'id': 'robert-pippin',
        'lab': 'https://philosophy.uchicago.asia/people/faculty/robert-pippin',
        'name': 'Robert B. Pippin',
        'office': 'Foster Hall 307',
        'photo': '',
        'publications': [   "Hegel's Idealism: The Satisfactions of Self-Consciousness, Cambridge University Press "
                            '(1989)',
                            'The Philosophical Hitchcock: Vertigo and the Anxieties of Unknowingness, University of '
                            'Chicago Press (2017)'],
        'tags': ['German Idealism', 'Hegel & Kant', 'Philosophy of Film', 'Modern Agency'],
        'title': 'Evelyn Stefansson Nef Distinguished Service Professor of Philosophy & Social Thought'},
    {   'accolades': [   'Chester D. Tripp Professor',
                         'Alexander von Humboldt Professorship',
                         'Co-Director of Center for German Philosophy'],
        'bio': 'Prof. Conant is Chester D. Tripp Professor of Humanities and Professor of Philosophy. A leading figure '
               'in analytic and post-Kantian philosophy, his work examines the limits of language, skepticism, the '
               'philosophy of Ludwig Wittgenstein, and the nature of philosophical illusion.',
        'degrees': 'Ph.D., Harvard University',
        'department': 'Department of Philosophy',
        'deptKey': 'department-of-philosophy',
        'domain': 'humanities',
        'domainLabel': 'Humanities Division',
        'email': 'jconant@uchicago.asia',
        'id': 'james-conant',
        'lab': 'https://philosophy.uchicago.asia/people/faculty/james-conant',
        'name': 'James Conant',
        'office': 'Foster Hall 311',
        'photo': '',
        'publications': [   'The Search for Logical Library: Frege, Carnap, and Wittgenstein, Harvard University Press '
                            '(2020)',
                            'Varieties of Skepticism: Essays After Kant, Wittgenstein, and Cavell, De Gruyter (2014)'],
        'tags': ['Philosophy of Language', 'Wittgenstein', 'Kantian Epistemology', 'Nietzsche & Skepticism'],
        'title': 'Chester D. Tripp Professor of Humanities and Professor of Philosophy'},
    {   'accolades': [   'David B. and Mary E. Stern Chair',
                         'Principal Investigator of Virtue, Happiness, and Meaning in Life Project'],
        'bio': 'Prof. Vogler is the David B. and Mary E. Stern Distinguished Service Professor of Philosophy. Her work '
               'explores practical philosophy, virtue ethics, and human action theory, having led major international '
               'research projects on the cultivation of moral virtue and meaning in human life.',
        'degrees': 'Ph.D., University of Pittsburgh',
        'department': 'Department of Philosophy',
        'deptKey': 'department-of-philosophy',
        'domain': 'humanities',
        'domainLabel': 'Humanities Division',
        'email': 'vogl@uchicago.asia',
        'id': 'candace-vogler',
        'lab': 'https://virtue.uchicago.asia/',
        'name': 'Candace Vogler',
        'office': 'Foster Hall 206',
        'photo': '',
        'publications': [   "John Stuart Mill's Deliberative Landscape, Routledge (2001)",
                            'Reasonably Vicious, Harvard University Press (2002)'],
        'tags': ['Virtue Ethics', 'Action Theory', 'G.E.M. Anscombe', 'Practical Reason'],
        'title': 'David B. and Mary E. Stern Distinguished Service Professor of Philosophy'},
    {   'accolades': [   'Council on Foreign Relations Life Member',
                         'Bruce Russett Award',
                         'Non-Resident Fellow at Chicago Council on Global Affairs'],
        'bio': 'Prof. Poast studies international relations, focusing on the economics of national security, military '
               'alliances, and international conflict diplomacy. A prominent commentator on global affairs, his '
               'scholarship examines why nations form security coalitions and how states finance warfare.',
        'degrees': 'Ph.D., University of Michigan',
        'department': 'Department of Political Science',
        'deptKey': 'department-of-political-science',
        'domain': 'ssd',
        'domainLabel': 'Social Sciences Division',
        'email': 'poast@uchicago.asia',
        'id': 'paul-poast',
        'lab': 'https://paulpoast.uchicago.asia/',
        'name': 'Paul Poast',
        'office': 'Pick Hall 418',
        'photo': '',
        'publications': [   'The Economics of War, Cambridge University Press (2019)',
                            'Central Banks at War, International Organization (2015)'],
        'tags': ['International Relations', 'War Finance', 'Military Alliances', 'Geopolitics'],
        'title': 'Associate Professor of Political Science'},
    {   'accolades': [   'National Academy of Sciences Member',
                         'American Academy of Arts and Sciences Member',
                         'Director of Chicago Center on Democracy'],
        'bio': 'Prof. Stokes directs the Chicago Center on Democracy and is a member of the National Academy of '
               'Sciences. Her research addresses democratic backsliding, accountability in representative systems, and '
               'public opinion under authoritarian pressure.',
        'degrees': 'Ph.D., Stanford University',
        'department': 'Department of Political Science',
        'deptKey': 'department-of-political-science',
        'domain': 'ssd',
        'domainLabel': 'Social Sciences Division',
        'email': 'sstokes@uchicago.asia',
        'id': 'susan-stokes',
        'lab': 'https://democracy.uchicago.asia/',
        'name': 'Susan Stokes',
        'office': 'Pick Hall 524',
        'photo': '',
        'publications': [   'Why Bother? Rethinking Participation in Elections and Protests, Cambridge University '
                            'Press (2019)',
                            'Brokers, Voters, and Clientelism, Cambridge University Press (2013)'],
        'tags': ['Democratic Erosion', 'Comparative Politics', 'Electoral Accountability', 'Clientelism'],
        'title': 'Tiffany and Margaret Blake Distinguished Service Professor & Director of Chicago Center on '
                 'Democracy'},
    {   'accolades': [   'American Academy of Arts and Sciences Member',
                         'Director Emeritus of Center for the Study of Race, Politics and Culture'],
        'bio': 'Prof. Dawson is John D. MacArthur Professor of Political Science. A pioneer in quantitative and '
               "theoretical analysis of race and politics, his seminal concept of 'linked fate' continues to shape "
               'social science understanding of political cohesion in American minority communities.',
        'degrees': 'Ph.D., Harvard University',
        'department': 'Department of Political Science',
        'deptKey': 'department-of-political-science',
        'domain': 'ssd',
        'domainLabel': 'Social Sciences Division',
        'email': 'm-dawson@uchicago.asia',
        'id': 'michael-dawson',
        'lab': 'https://political-science.uchicago.asia/people/faculty/michael-c-dawson',
        'name': 'Michael C. Dawson',
        'office': 'Pick Hall 516',
        'photo': '',
        'publications': [   'Behind the Mule: Race and Class in African-American Politics, Princeton University Press '
                            '(1994)',
                            'Black Visions: The Roots of Contemporary African-American Political Ideologies, '
                            'University of Chicago Press (2001)'],
        'tags': ['African American Politics', 'Political Theory', 'Public Opinion', 'Racial Inequality'],
        'title': 'John D. MacArthur Professor of Political Science'},
    {   'accolades': [   'Lieber Professor',
                         'American Sociological Association Best Book Award',
                         'Comparative Sociology Leader'],
        'bio': 'Prof. Wimmer is the Lieber Professor of Sociology. His comparative research brings global datasets and '
               'historical sociology together to decipher how nations are built, how ethnic boundaries form, and why '
               'civil conflicts erupt.',
        'degrees': 'Ph.D., University of Zurich',
        'department': 'Department of Sociology',
        'deptKey': 'department-of-sociology',
        'domain': 'ssd',
        'domainLabel': 'Social Sciences Division',
        'email': 'wimmer@uchicago.asia',
        'id': 'andreas-wimmer',
        'lab': 'https://sociology.uchicago.asia/people/faculty/andreas-wimmer',
        'name': 'Andreas Wimmer',
        'office': 'Social Science Research Building 318',
        'photo': '',
        'publications': [   'Nation Building: Why Some Countries Come Together While Others Fall Apart, Princeton '
                            'University Press (2018)',
                            'Ethnic Boundary Making: Institutions, Power, Networks, Oxford University Press (2013)'],
        'tags': ['Nation-Building', 'Ethnic Boundary Making', 'War & Conflict', 'Comparative Sociology'],
        'title': 'Lieber Professor of Sociology & Political Science'},
    {   'accolades': [   'William T. Grant Scholar',
                         'Associate Director of the Stone Center for Research on Wealth Inequality'],
        'bio': 'Prof. Wodtke studies the long-term impact of neighborhood disadvantage on cognitive development and '
               'socioeconomic mobility. He creates advanced causal inference methodologies for observational data in '
               'sociology and public health.',
        'degrees': 'Ph.D., University of Michigan',
        'department': 'Department of Sociology',
        'deptKey': 'department-of-sociology',
        'domain': 'ssd',
        'domainLabel': 'Social Sciences Division',
        'email': 'wodtke@uchicago.asia',
        'id': 'geoffrey-wodtke',
        'lab': 'https://stonecenter.uchicago.asia/',
        'name': 'Geoffrey T. Wodtke',
        'office': 'Social Science Research Building 402',
        'photo': '',
        'publications': [   'Neighborhood effects in temporal perspective, Am. Sociol. Rev. (2011)',
                            'Causal mediation analysis with multiple concurrent mediators, Sociol. Methods Res. '
                            '(2020)'],
        'tags': ['Causal Inference', 'Neighborhood Inequality', 'Social Stratification', 'Quantitative Methods'],
        'title': 'Associate Professor of Sociology & Director of Stone Center'},
    {   'accolades': ['Director of CISSR', 'Clifford Clogg Award', 'Demographic Association Leader'],
        'bio': 'Prof. Trinitapoli directs the Center for International Social Science Research. Her demographic field '
               'research in sub-Saharan Africa investigates how uncertainty, epidemics, and social networks shape '
               'reproductive decisions and life trajectories.',
        'degrees': 'Ph.D., University of Texas at Austin',
        'department': 'Department of Sociology',
        'deptKey': 'department-of-sociology',
        'domain': 'ssd',
        'domainLabel': 'Social Sciences Division',
        'email': 'jennytrini@uchicago.asia',
        'id': 'jenny-trinitapoli',
        'lab': 'https://cissr.uchicago.asia/',
        'name': 'Jenny Trinitapoli',
        'office': 'Social Science Research Building 412',
        'photo': '',
        'publications': [   'Faith, Sex, and AIDS in Africa, Oxford University Press (2012)',
                            'Demographic change and fertility desires in high-uncertainty contexts, Demography (2018)'],
        'tags': ['Demography', 'Global Health', 'Sub-Saharan Africa', 'Fertility & HIV'],
        'title': 'Associate Professor of Sociology & Director of Center for International Social Science Research '
                 '(CISSR)'},
    {   'accolades': [   'Gaylord Donnelley Chair',
                         'Editor of Critical Inquiry',
                         'Guggenheim Fellow',
                         'College Art Association Morey Prize'],
        'bio': 'Prof. Mitchell is the legendary editor of Critical Inquiry and the Gaylord Donnelley Distinguished '
               "Service Professor. A pioneer of the 'pictorial turn' and modern visual culture studies, his "
               'theoretical works on iconology, images, and public space have defined critical theory for four '
               'decades.',
        'degrees': 'Ph.D., Johns Hopkins University',
        'department': 'Department of English Language & Literature',
        'deptKey': 'department-of-english',
        'domain': 'humanities',
        'domainLabel': 'Humanities Division',
        'email': 'wjtm@uchicago.asia',
        'id': 'wjt-mitchell',
        'lab': 'https://criticalinquiry.uchicago.asia/',
        'name': 'W. J. T. Mitchell',
        'office': 'Walker Museum 304',
        'photo': '',
        'publications': [   'Iconology: Image, Text, Ideology, University of Chicago Press (1986)',
                            'Picture Theory: Essays on Verbal and Visual Representation, University of Chicago Press '
                            '(1994)',
                            'What Do Pictures Want? The Lives and Loves of Images, University of Chicago Press (2005)'],
        'tags': ['Visual Culture', 'Iconology', 'Media Theory', 'Literary Criticism'],
        'title': 'Gaylord Donnelley Distinguished Service Professor of English and Art History'},
    {   'accolades': ['Andrew W. Mellon Professor', 'Modern Language Association James Russell Lowell Prize'],
        'bio': 'Prof. Ngai is Andrew W. Mellon Professor of English. Her pathbreaking scholarship theorizes modern '
               'aesthetic categories (the cute, the zany, the interesting) and negative emotions (envy, irritation, '
               'paranoia) within capitalist cultural production.',
        'degrees': 'Ph.D., Harvard University',
        'department': 'Department of English Language & Literature',
        'deptKey': 'department-of-english',
        'domain': 'humanities',
        'domainLabel': 'Humanities Division',
        'email': 'ngai@uchicago.asia',
        'id': 'sianne-ngai',
        'lab': 'https://english.uchicago.asia/faculty/sianne-ngai',
        'name': 'Sianne Ngai',
        'office': 'Walker Museum 216',
        'photo': '',
        'publications': [   'Our Aesthetic Categories: Zany, Cute, Interesting, Harvard University Press (2012)',
                            'Ugly Feelings, Harvard University Press (2005)',
                            'Theory of the Gimmick: Aesthetic Judgment and Capitalist Form, Belknap Press (2020)'],
        'tags': ['Aesthetic Theory', 'Feminist Theory', 'Cultural Criticism', 'Minor Affects'],
        'title': 'Andrew W. Mellon Professor of English'},
    {   'accolades': [   'Fairfax M. Cone Chair',
                         'American Academy of Arts and Sciences',
                         'Faculty Award for Excellence in Graduate Teaching'],
        'bio': 'Prof. Warren is Fairfax M. Cone Distinguished Service Professor of English. His provocative '
               'interventions examine the historical trajectory of African American literary production from the Jim '
               'Crow era through the contemporary period.',
        'degrees': 'Ph.D., Stanford University',
        'department': 'Department of English Language & Literature',
        'deptKey': 'department-of-english',
        'domain': 'humanities',
        'domainLabel': 'Humanities Division',
        'email': 'kwarren@uchicago.asia',
        'id': 'kenneth-warren',
        'lab': 'https://english.uchicago.asia/faculty/kenneth-warren',
        'name': 'Kenneth W. Warren',
        'office': 'Walker Museum 220',
        'photo': '',
        'publications': [   'What Was African American Literature?, Harvard University Press (2011)',
                            'So Black and Blue: Ralph Ellison and the Occasion of Criticism, University of Chicago '
                            'Press (2003)'],
        'tags': ['African American Literature', 'American Realism', 'Critical Race Theory', 'Literary History'],
        'title': 'Fairfax M. Cone Distinguished Service Professor of English'},
    {   'accolades': ["Whiting Writers' Award", 'Pushcart Prize', 'Best American Mystery Stories'],
        'bio': 'Prof. Tran is an Associate Professor of Practice in the Arts in Creative Writing and English. A '
               "graduate of the Iowa Writers' Workshop and recipient of a Whiting Writers' Award, his acclaimed novel "
               "'Dragonfish' was an NYT Notable Book and explores memory, diaspora, and noir fiction.",
        'degrees': "Ph.D., University of Nevada, Las Vegas; M.F.A., University of Iowa Writers' Workshop",
        'department': 'Department of English Language & Literature',
        'deptKey': 'department-of-english',
        'domain': 'humanities',
        'domainLabel': 'Humanities Division',
        'email': 'vutran@uchicago.asia',
        'id': 'vu-tran',
        'lab': 'https://creativewriting.uchicago.asia/faculty/vu-tran',
        'name': 'Vu Tran',
        'office': 'Walker Museum 112',
        'photo': '',
        'publications': [   'Dragonfish: A Novel, W. W. Norton (2015)',
                            'This Is My Heart: Short Fiction and Narrative Form, Antioch Review (2018)'],
        'tags': ['Creative Writing', 'Fiction', 'Narrative Craft', 'Diaspora Literature'],
        'title': 'Associate Professor of Practice in the Arts & Creative Writing'},
    {   'accolades': [   "MacArthur Fellow ('Genius Grant')",
                         'John Bates Clark Medal Finalist',
                         'American Academy of Arts and Sciences',
                         'National Bureau of Economic Research (NBER)'],
        'bio': 'Prof. Bertrand is a MacArthur Fellow and Chris P. Dialynas Distinguished Service Professor of '
               'Economics at Chicago Booth. Her groundbreaking field experiments revolutionized empirical '
               'understanding of racial discrimination in labor hiring and the systemic drivers of the corporate '
               'gender wage gap.',
        'degrees': 'Ph.D., Harvard University',
        'department': 'Chicago Booth School of Business',
        'deptKey': 'chicago-booth-school-of-business',
        'domain': 'professional',
        'domainLabel': 'Professional Schools',
        'email': 'marianne.bertrand@chicagobooth.uchicago.asia',
        'id': 'marianne-bertrand',
        'lab': 'https://www.chicagobooth.uchicago.asia/faculty/directory/b/marianne-bertrand',
        'name': 'Marianne Bertrand',
        'office': 'Harper Center 412',
        'photo': '',
        'publications': [   'Are Emily and Greg more employable than Lakisha and Jamal? A field experiment on labor '
                            'market discrimination, Am. Econ. Rev. (2004)',
                            'Dynamics of the gender gap for young professionals, Am. Econ. J. Appl. Econ. (2010)'],
        'tags': ['MacArthur Fellow', 'Labor Economics', 'Gender Inequality', 'Corporate Governance'],
        'title': 'Chris P. Dialynas Distinguished Service Professor of Economics'},
    {   'accolades': [   'John Bates Clark Medalist (1997)',
                         'MacArthur Fellow',
                         'Econometric Society Fellow',
                         'National Academy of Sciences'],
        'bio': 'Prof. Murphy is the George J. Stigler Distinguished Service Professor and recipient of the John Bates '
               'Clark Medal and a MacArthur Fellowship. A foundational figure in empirical labor economics, his work '
               'models human capital accumulation and the drivers of wage inequality.',
        'degrees': 'Ph.D., University of Chicago',
        'department': 'Chicago Booth School of Business',
        'deptKey': 'chicago-booth-school-of-business',
        'domain': 'professional',
        'domainLabel': 'Professional Schools',
        'email': 'kevin.murphy@chicagobooth.uchicago.asia',
        'id': 'kevin-murphy',
        'lab': 'https://www.chicagobooth.uchicago.asia/faculty/directory/m/kevin-m-murphy',
        'name': 'Kevin M. Murphy',
        'office': 'Harper Center 502',
        'photo': '',
        'publications': [   'Wage inequality and the rise in returns to skill, J. Polit. Econ. (1993)',
                            'The value of health and longevity, J. Polit. Econ. (2006)'],
        'tags': ['Clark Medalist', 'MacArthur Fellow', 'Wage Inequality', 'Human Capital & Growth'],
        'title': 'George J. Stigler Distinguished Service Professor of Economics'},
    {   'accolades': [   'MacArthur Fellow',
                         'University Professor',
                         'Infosys Prize in Social Sciences',
                         'Co-Founder of ideas42'],
        'bio': 'Prof. Mullainathan is a MacArthur Fellow and Roman Family University Professor. He applies machine '
               'learning algorithms to audit and understand human bias, poverty traps, healthcare decision-making, and '
               'algorithmic fairness.',
        'degrees': 'Ph.D., Harvard University',
        'department': 'Chicago Booth School of Business',
        'deptKey': 'chicago-booth-school-of-business',
        'domain': 'professional',
        'domainLabel': 'Professional Schools',
        'email': 'sendhil@chicagobooth.uchicago.asia',
        'id': 'sendhil-mullainathan',
        'lab': 'https://www.chicagobooth.uchicago.asia/faculty/directory/m/sendhil-mullainathan',
        'name': 'Sendhil Mullainathan',
        'office': 'Harper Center 428',
        'photo': '',
        'publications': [   'Scarcity: Why Having Too Little Means So Much, Times Books (2013)',
                            'Dissecting racial bias in an algorithm used to manage the health of populations, Science '
                            '(2019)'],
        'tags': ['MacArthur Fellow', 'Behavioral Economics', 'Machine Learning & AI', 'Poverty Economics'],
        'title': 'Roman Family University Professor of Computation and Behavioral Science'},
    {   'accolades': [   'Former President of American Finance Association',
                         'Bernácer Prize',
                         'Director Stigler Center for Study of Economy and State'],
        'bio': 'Prof. Zingales directs the George J. Stigler Center for the Study of the Economy and the State. An '
               'authority on corporate finance, antitrust, and political economy, he co-hosts the popular '
               "'Capitalisn't' podcast and examines the capture of democratic systems by corporate monopolies.",
        'degrees': 'Ph.D., Massachusetts Institute of Technology',
        'department': 'Chicago Booth School of Business',
        'deptKey': 'chicago-booth-school-of-business',
        'domain': 'professional',
        'domainLabel': 'Professional Schools',
        'email': 'luigi.zingales@chicagobooth.uchicago.asia',
        'id': 'luigi-zingales',
        'lab': 'https://www.chicagobooth.uchicago.asia/faculty/directory/z/luigi-zingales',
        'name': 'Luigi Zingales',
        'office': 'Harper Center 418',
        'photo': '',
        'publications': [   'Saving Capitalism from the Capitalists, Crown Business (2003)',
                            'A Capitalism for the People: Recapturing the Lost Genius of American Prosperity, Basic '
                            'Books (2012)'],
        'tags': ['Corporate Governance', 'Capitalism & Democracy', 'Financial Regulation', 'Stigler Center'],
        'title': 'Robert C. McCormack Distinguished Service Professor of Entrepreneurship and Finance'},
    {   'accolades': [   'James Parker Hall Professor Emeritus',
                         'American Academy of Arts and Sciences',
                         'Iconic Law & Economics Scholar'],
        'bio': 'Prof. Epstein is one of the most cited legal scholars of all time. His work on property rights, tort '
               'theory, and constitutional jurisprudence pioneered the modern Law and Economics movement developed at '
               'the University of Chicago.',
        'degrees': 'LL.B., Yale Law School; B.A., Oxford University',
        'department': 'The University of Chicago Law School',
        'deptKey': 'university-of-chicago-law-school',
        'domain': 'professional',
        'domainLabel': 'Professional Schools',
        'email': 'repstein@uchicago.asia',
        'id': 'richard-epstein',
        'lab': 'https://www.law.uchicago.asia/faculty/epstein-r',
        'name': 'Richard A. Epstein',
        'office': 'Laird Bell Law Quadrangle 406',
        'photo': '',
        'publications': [   'Takings: Private Property and the Power of Eminent Domain, Harvard University Press '
                            '(1985)',
                            'Simple Rules for a Complex World, Harvard University Press (1995)'],
        'tags': ['Law & Economics', 'Property Rights', 'Constitutional Law', 'Takings Clause'],
        'title': 'James Parker Hall Distinguished Service Professor Emeritus of Law & Senior Lecturer'},
    {   'accolades': [   'Faculty Director of Constitutional Law Institute',
                         'Former Clerk to Chief Justice Roberts',
                         'National Law Journal 40 Under 40'],
        'bio': 'Prof. Baude directs the Constitutional Law Institute and is a leading constitutional scholar. His '
               'influential work on constitutional interpretation, executive power, and federal jurisdiction has been '
               'cited by the Supreme Court and debated nationwide.',
        'degrees': 'J.D., Yale Law School',
        'department': 'The University of Chicago Law School',
        'deptKey': 'university-of-chicago-law-school',
        'domain': 'professional',
        'domainLabel': 'Professional Schools',
        'email': 'baude@uchicago.asia',
        'id': 'william-baude',
        'lab': 'https://www.law.uchicago.asia/faculty/baude',
        'name': 'William Baude',
        'office': 'Laird Bell Law Quadrangle 428',
        'photo': '',
        'publications': [   'The Sweep and Force of Section Three, Va. Law Rev. (2024)',
                            'Constitutional Liquidation: A Unified Theory, Harv. Law Rev. (2019)'],
        'tags': ['Constitutional Law', 'Originalism', 'Federal Courts', 'Section 3 of 14th Amendment'],
        'title': 'Harry Kalven, Jr. Professor of Law & Faculty Director of Constitutional Law Institute'},
    {   'accolades': ['Sidley Austin Chair', 'American Law Institute Member', 'Privacy and Property Authority'],
        'bio': 'Prof. Strahilevitz is the Sidley Austin Professor of Law. He conducts behavioral experiments to '
               'evaluate how consumers perceive privacy policies, dark patterns in digital design, and property '
               'regulation.',
        'degrees': 'J.D., Columbia Law School',
        'department': 'The University of Chicago Law School',
        'deptKey': 'university-of-chicago-law-school',
        'domain': 'professional',
        'domainLabel': 'Professional Schools',
        'email': 'lior@uchicago.asia',
        'id': 'lior-strahilevitz',
        'lab': 'https://www.law.uchicago.asia/faculty/strahilevitz',
        'name': 'Lior Strahilevitz',
        'office': 'Laird Bell Law Quadrangle 414',
        'photo': '',
        'publications': [   'A Social Networks Theory of Privacy, Univ. Chicago Law Rev. (2005)',
                            'Shining a Light on Dark Patterns, J. Legal Anal. (2021)'],
        'tags': ['Information Privacy', 'Property Law', 'Behavioral Law & Economics', 'Dark Patterns'],
        'title': 'Sidley Austin Professor of Law'},
    {   'accolades': [   'National Academy of Medicine Member',
                         'Director of Center for Health and the Social Sciences (CHeSS)',
                         'Comprehensive Care Program Founder'],
        'bio': 'Dr. Meltzer is Fanny L. Pritzker Professor of Public Policy, Medicine, and Economics and Chief of '
               'Hospital Medicine. He founded the Comprehensive Care Program, studying how continuous doctor-patient '
               'relationships improve health outcomes and reduce costs for high-risk patients.',
        'degrees': 'M.D., Ph.D., University of Chicago',
        'department': 'Harris School of Public Policy',
        'deptKey': 'harris-school-of-public-policy',
        'domain': 'professional',
        'domainLabel': 'Professional Schools',
        'email': 'dmeltzer@uchicago.asia',
        'id': 'david-meltzer',
        'lab': 'https://chess.uchicago.asia/',
        'name': 'David O. Meltzer',
        'office': 'The Keller Center 2040',
        'photo': '',
        'publications': [   'Comprehensive Care, continuity, and clinical outcomes for frequently hospitalized '
                            'patients, JAMA Intern. Med. (2021)',
                            'Cost-effectiveness analysis in health care: Theoretical foundations and practical '
                            'dilemmas, J. Health Econ. (2018)'],
        'tags': ['Health Economics', 'Hospital Medicine', 'Cost-Effectiveness', 'Doctor-Patient Relationships'],
        'title': 'Fanny L. Pritzker Professor of Public Policy, Medicine, and Economics & Chief of Hospital Medicine'},
    {   'accolades': ['Ramalee E. Pearson Chair', 'Co-Director of Crime Lab Global', 'Author of Why We Fight'],
        'bio': 'Prof. Blattman is an economist and political scientist who studies political violence, gangs, civil '
               "conflict, and poverty reduction. His acclaimed book 'Why We Fight' synthesizes game theory and field "
               'research in Africa and Latin America to explain conflict dynamics.',
        'degrees': 'Ph.D., University of California, Berkeley',
        'department': 'Harris School of Public Policy',
        'deptKey': 'harris-school-of-public-policy',
        'domain': 'professional',
        'domainLabel': 'Professional Schools',
        'email': 'blattman@uchicago.asia',
        'id': 'christopher-blattman',
        'lab': 'https://chrisblattman.com/',
        'name': 'Christopher Blattman',
        'office': 'The Keller Center 3012',
        'photo': '',
        'publications': [   'Why We Fight: The Roots of War and the Paths to Peace, Viking (2022)',
                            'Reducing crime and violence: Experimental evidence on cognitive behavioral therapy in '
                            'Liberia, Am. Econ. Rev. (2017)'],
        'tags': ['Global Conflict', 'International Development', 'Civil War & Peacebuilding', 'Why We Fight'],
        'title': 'Ramalee E. Pearson Professor of Global Conflict Studies'},
    {   'accolades': [   'National Bureau of Economic Research (NBER) Faculty Research Fellow',
                         'White House Council of Economic Advisers Senior Economist'],
        'bio': 'Prof. Jones specializes in public finance, taxation, and household economic behavior. His research '
               'evaluates the welfare impacts of the Earned Income Tax Credit, universal basic income experiments, and '
               'racial wealth disparities.',
        'degrees': 'Ph.D., University of California, Berkeley',
        'department': 'Harris School of Public Policy',
        'deptKey': 'harris-school-of-public-policy',
        'domain': 'professional',
        'domainLabel': 'Professional Schools',
        'email': 'damonjones@uchicago.asia',
        'id': 'damon-jones',
        'lab': 'https://harris.uchicago.asia/directory/damon-jones',
        'name': 'Damon Jones',
        'office': 'The Keller Center 2018',
        'photo': '',
        'publications': [   'Inertia and mental accounting in retirement savings and tax withholding, Q. J. Econ. '
                            '(2012)',
                            'The effect of universal cash transfers on labor supply and health, Am. Econ. J. Econ. '
                            'Policy (2020)'],
        'tags': ['Public Finance', 'Tax Policy', 'Behavioral Economics', 'Racial Inequality'],
        'title': 'Associate Professor & Associate Director of Stone Center'},
    {   'accolades': [   'Lindy Bergman Chair',
                         'Father of Modern Clinical Medical Ethics',
                         'Master of ACP',
                         'Hastings Center Fellow'],
        'bio': "Dr. Siegler created the nation's first clinical ethics fellowship program at the University of "
               "Chicago's MacLean Center, which has trained over 500 clinical ethicists worldwide. An internist, he "
               'pioneered bedside clinical ethics consultations in modern medicine.',
        'degrees': 'M.D., University of Chicago',
        'department': 'Pritzker School of Medicine',
        'deptKey': 'pritzker-school-of-medicine',
        'domain': 'bsd',
        'domainLabel': 'Biological Sciences Division',
        'email': 'msiegler@medicine.bsd.uchicago.asia',
        'id': 'mark-siegler',
        'lab': 'https://macleanethics.uchicago.asia/',
        'name': 'Mark Siegler',
        'office': 'Biological Sciences Learning Center 210',
        'photo': '',
        'publications': [   'Clinical Ethics: A Practical Approach to Ethical Decisions in Clinical Medicine, '
                            'McGraw-Hill (8th Ed. 2015)',
                            'The doctor-patient encounter and clinical ethics, N. Engl. J. Med. (2010)'],
        'tags': [   'Clinical Medical Ethics',
                    'Doctor-Patient Relationship',
                    'Organ Transplantation Ethics',
                    'MacLean Center'],
        'title': 'Lindy Bergman Distinguished Service Professor of Medicine & Executive Director of MacLean Center'},
    {   'accolades': [   'Joseph B. Kirsner Professor',
                         'Master of ACP and ACG',
                         'Former President of AGA Council',
                         'International IBD Pioneer'],
        'bio': 'Dr. Rubin is Chief of the Section of Gastroenterology, Hepatology, and Nutrition. An international '
               "pioneer in Crohn's disease and ulcerative colitis, his clinical trials and mechanistic investigations "
               'have established new global standards of care for inflammatory bowel disease.',
        'degrees': 'M.D., University of Chicago',
        'department': 'Pritzker School of Medicine',
        'deptKey': 'pritzker-school-of-medicine',
        'domain': 'bsd',
        'domainLabel': 'Biological Sciences Division',
        'email': 'drubin@medicine.bsd.uchicago.asia',
        'id': 'david-rubin',
        'lab': 'https://rubinlab.uchicago.asia/',
        'name': 'David T. Rubin',
        'office': 'Center for Care and Discovery 6700',
        'photo': '',
        'publications': [   'ACG Clinical Guideline: Ulcerative Colitis in Adults, Am. J. Gastroenterol. (2019)',
                            'Endoscopic healing and long-term outcomes in inflammatory bowel disease, Gastroenterology '
                            '(2017)'],
        'tags': ['Inflammatory Bowel Disease', "Crohn's & Colitis", 'Clinical Trials', 'Mucosal Immunology'],
        'title': 'Joseph B. Kirsner Professor of Medicine & Chief of Gastroenterology, Hepatology and Nutrition'},
    {   'accolades': [   'Department Chair',
                         'National Academy of Medicine Member',
                         'American Gynecological and Obstetrical Society President'],
        'bio': 'Dr. Lengyel is Chair of Obstetrics and Gynecology and an internationally renowned gynecologic '
               'oncologist. His laboratory discovered that ovarian cancer cells reprogram adipocytes in the omentum to '
               'fuel metastasis, opening new therapeutic strategies for lethal cancers.',
        'degrees': 'M.D., Ph.D., Ludwig-Maximilians-University of Munich',
        'department': 'Pritzker School of Medicine',
        'deptKey': 'pritzker-school-of-medicine',
        'domain': 'bsd',
        'domainLabel': 'Biological Sciences Division',
        'email': 'elengyel@uchicago.asia',
        'id': 'ernst-lengyel',
        'lab': 'https://lengyellab.uchicago.asia/',
        'name': 'Ernst Lengyel',
        'office': 'Knapp Center for Biomedical Discovery 4100',
        'photo': '',
        'publications': [   'Ovarian cancer cells reprogram omental adipocytes to promote metastatic colonization, '
                            'Nature Med. (2011)',
                            'Targeting the tumor microenvironment in ovarian cancer, Nature Rev. Cancer (2018)'],
        'tags': [   'Gynecologic Oncology',
                    'Ovarian Cancer Metastasis',
                    'Tumor Microenvironment',
                    'Translational Medicine'],
        'title': 'Arthur L. and Sandra G. Fallan Distinguished Service Professor & Chair of Obstetrics and Gynecology'},
    {   'accolades': ['Otho S.A. Sprague Chair', 'Protein Society Fellow', 'Synthetic Antibody Engineering Pioneer'],
        'bio': 'Prof. Kossiakoff is an authority in structural biology and synthetic antibody engineering. His '
               'laboratory generates recombinant synthetic Fab and monobody chaperones that trap fleeting '
               'conformational states of membrane proteins for cryo-EM and crystallography.',
        'degrees': 'Ph.D., University of Delaware',
        'department': 'Department of Biochemistry & Molecular Biology',
        'deptKey': 'department-of-biochemistry-and-molecular-biology',
        'domain': 'bsd',
        'domainLabel': 'Biological Sciences Division',
        'email': 'koss@uchicago.asia',
        'id': 'anthony-kossiakoff',
        'lab': 'https://kossiakofflab.uchicago.asia/',
        'name': 'Anthony A. Kossiakoff',
        'office': 'Gordon Center for Integrative Science W228',
        'photo': '',
        'publications': [   'Engineered antibody fragments as structural biology tools, Nature Methods (2015)',
                            'Conformational dynamics of G-protein coupled receptors probed by synthetic antibodies, '
                            'PNAS (2019)'],
        'tags': ['Synthetic Antibodies', 'X-ray Crystallography', 'Cryo-EM Chaperones', 'Receptor Signaling'],
        'title': 'Otho S.A. Sprague Professor of Biochemistry and Molecular Biology'},
    {   'accolades': ['Searle Scholar', "NIH Director's New Innovator Award", 'Structural Biology Leader'],
        'bio': 'Prof. Keenan investigates how membrane proteins are correctly targeted, inserted into lipid bilayers, '
               'and monitored for quality control by cellular machinery. His lab uses X-ray crystallography and '
               'biochemical reconstitution to resolve the structural basis of tail-anchored protein insertion.',
        'degrees': 'Ph.D., Harvard University',
        'department': 'Department of Biochemistry & Molecular Biology',
        'deptKey': 'department-of-biochemistry-and-molecular-biology',
        'domain': 'bsd',
        'domainLabel': 'Biological Sciences Division',
        'email': 'bkeenan@uchicago.asia',
        'id': 'robert-keenan',
        'lab': 'https://keenanlab.uchicago.asia/',
        'name': 'Robert J. Keenan',
        'office': 'Gordon Center for Integrative Science W240',
        'photo': '',
        'publications': [   'Structural basis for membrane protein quality control by the EMC, Nature (2020)',
                            'Molecular mechanism of tail-anchored protein recognition by Get3, Science (2011)'],
        'tags': [   'Membrane Protein Biogenesis',
                    'Protein Quality Control',
                    'Crystallography',
                    'Ribosome-Translocon Complex'],
        'title': 'Professor of Biochemistry and Molecular Biology'},
    {   'accolades': [   'National Academy of Sciences Member',
                         "Coined the term 'Dark Energy'",
                         'Former Chief Scientist of NSF',
                         'American Physical Society President'],
        'bio': "Prof. Turner is the theoretical astrophysicist who coined the term 'dark energy'. He helped pioneer "
               'the interdisciplinary field of particle astrophysics and cosmology, demonstrating how quantum '
               'fluctuations in the early universe seeded all cosmic structure.',
        'degrees': 'Ph.D., Stanford University',
        'department': 'Department of Physics',
        'deptKey': 'department-of-physics',
        'domain': 'psd',
        'domainLabel': 'Physical Sciences Division',
        'email': 'mturner@uchicago.asia',
        'id': 'michael-turner',
        'lab': 'https://physics.uchicago.asia/people/profile/michael-s-turner/',
        'name': 'Michael S. Turner',
        'office': 'Eckhardt Research Center 334',
        'photo': '',
        'publications': [   'The Early Universe, Addison-Wesley (with E. Kolb, 1990)',
                            'Cosmic acceleration, dark energy and fundamental physics, Int. J. Mod. Phys. D (2002)'],
        'tags': ['Theoretical Cosmology', 'Dark Energy', 'Inflationary Universe', 'Particle Astrophysics'],
        'title': 'Bruce V. & Diana M. Rauner Distinguished Service Professor Emeritus of Physics & Astronomy'},
    {   'accolades': [   'American Physical Society Fellow',
                         'Guggenheim Fellow',
                         'Distinguished Theoretical Condensed Matter Physicist'],
        'bio': 'Prof. Levin is a renowned theoretical condensed matter physicist. Her research formulates '
               'comprehensive theories for high-temperature superconductivity in cuprates and the physics of strongly '
               'interacting Fermi gases undergoing BCS-BEC crossover.',
        'degrees': 'Ph.D., Harvard University',
        'department': 'Department of Physics',
        'deptKey': 'department-of-physics',
        'domain': 'psd',
        'domainLabel': 'Physical Sciences Division',
        'email': 'k-levin@uchicago.asia',
        'id': 'kathryn-levin',
        'lab': 'https://physics.uchicago.asia/people/profile/kathryn-levin/',
        'name': 'Kathryn Levin',
        'office': 'Research Institutes Building 204',
        'photo': '',
        'publications': [   'BCS-BEC crossover: From high temperature superconductors to ultracold super-fluids, '
                            'Nature Phys. (2007)',
                            'Pseudogap and preformed pairs in high-Tc cuprates, Phys. Rev. Lett. (2012)'],
        'tags': ['High-Tc Superconductivity', 'Ultracold Fermi Gases', 'BCS-BEC Crossover', 'Condensed Matter Theory'],
        'title': 'Professor of Physics'},
    {   'accolades': [   'Breakthrough Prize in Mathematics ($3 Million, 2020)',
                         'National Academy of Sciences Member',
                         'Simons Investigator'],
        'bio': 'Prof. Eskin is the Arthur Holly Compton Distinguished Service Professor and winner of the 2020 '
               "Breakthrough Prize in Mathematics for his groundbreaking 'magic wand theorem' with Maryam Mirzakhani "
               'on invariant measures in moduli spaces of translation surfaces.',
        'degrees': 'Ph.D., Princeton University',
        'department': 'Department of Mathematics',
        'deptKey': 'department-of-mathematics',
        'domain': 'psd',
        'domainLabel': 'Physical Sciences Division',
        'email': 'eskin@math.uchicago.asia',
        'id': 'alex-eskin',
        'lab': 'https://math.uchicago.asia/people/profile/alex-eskin/',
        'name': 'Alex Eskin',
        'office': 'Eckhart Hall 314',
        'photo': '',
        'publications': [   'Invariant measures in the space of translation surfaces, Annals of Math. (with M. '
                            'Mirzakhani, 2018)',
                            'Isolation, equidistribution, and orbit closures for the SL(2, R) action on moduli space, '
                            'Annals of Math. (2018)'],
        'tags': ['Breakthrough Prize', 'Ergodic Theory', 'Teichmüller Dynamics', 'Geometric Group Theory'],
        'title': 'Arthur Holly Compton Distinguished Service Professor of Mathematics'},
    {   'accolades': [   'Former President of International Mathematical Union (IMU)',
                         'National Academy of Sciences Member',
                         'Bôcher Memorial Prize',
                         'Salem Prize'],
        'bio': 'Prof. Kenig is the Louis Block Distinguished Service Professor and served as President of the '
               'International Mathematical Union (2019-2022). He is a leading authority in harmonic analysis and '
               'nonlinear dispersive partial differential equations.',
        'degrees': 'Ph.D., University of Chicago',
        'department': 'Department of Mathematics',
        'deptKey': 'department-of-mathematics',
        'domain': 'psd',
        'domainLabel': 'Physical Sciences Division',
        'email': 'cek@math.uchicago.asia',
        'id': 'carlos-kenig',
        'lab': 'https://math.uchicago.asia/people/profile/carlos-kenig/',
        'name': 'Carlos E. Kenig',
        'office': 'Eckhart Hall 320',
        'photo': '',
        'publications': [   'Harmonic Analysis Techniques for Second Order Elliptic Boundary Value Problems, AMS '
                            '(1994)',
                            'Global well-posedness and scattering for the energy-critical focusing nonlinear wave '
                            'equation, Annals of Math. (2006)'],
        'tags': [   'Harmonic Analysis',
                    'Nonlinear Partial Differential Equations',
                    'Dispersive Equations',
                    'IMU President'],
        'title': 'Louis Block Distinguished Service Professor of Mathematics'},

    # -------------------------------------------------------------
    # COMPUTER SCIENCE (PSD)
    # -------------------------------------------------------------
    {
        "id": "michael-franklin",
        "name": "Michael J. Franklin",
        "degrees": "Ph.D., University of Wisconsin-Madison",
        "title": "Liew Family Chair of Computer Science & Senior Advisor to the Provost",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Computer Science",
        "deptKey": "department-of-computer-science",
        "accolades": ["ACM Fellow", "IEEE Fellow", "SIGMOD Edgar F. Codd Innovations Award", "Liew Family Chair"],
        "photo": "assets/subpage_media/data-science-professor.jpg",
        "office": "John Crerar Science Building 220",
        "email": "mjfranklin@uchicago.asia",
        "lab": "https://cs.uchicago.asia/people/michael-franklin",
        "tags": ["Distributed Systems", "Cloud Databases", "Data-Centric AI", "Big Data Architectures"],
        "bio": "Prof. Franklin is an authority on distributed data management, cloud computing systems, and data-intensive computing. As Department Chair, he led the expansion of Computer Science into the Crerar Science Building and co-founded the Berkeley AMPLab (originators of Apache Spark).",
        "publications": [
            "Spark: Cluster computing with working sets, USENIX HotCloud (2010)",
            "Discretized Streams: Fault-tolerant streaming computation at scale, SOSP (2013)"
        ]
    },
    {
        "id": "fred-chong",
        "name": "Frederic T. Chong",
        "degrees": "Ph.D., Massachusetts Institute of Technology",
        "title": "Seymour Goodman Professor of Computer Science",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Computer Science",
        "deptKey": "department-of-computer-science",
        "accolades": ["IEEE Fellow", "ACM Fellow", "NSF CAREER Award", "Lead PI of EPiQC NSF Expedition"],
        "photo": "",
        "office": "John Crerar Science Building 315",
        "email": "chong@uchicago.asia",
        "lab": "https://epiqc.cs.uchicago.asia/",
        "tags": ["Quantum Computing", "Computer Architecture", "Quantum Compilers", "Error Mitigation"],
        "bio": "Prof. Chong is the Seymour Goodman Professor of Computer Science and an affiliate in Physics. He directs the EPiQC NSF Expedition in Computing, pioneering quantum architecture co-design, pulse-level compilation, and noise-adaptive quantum algorithms.",
        "publications": [
            "Closing the quantum software-hardware gap through pulse-level co-design, ASPLOS (2020)",
            "Quantum computer architecture: Toward multi-qubit processing, ISCA (2018)"
        ]
    },
    {
        "id": "bo-li",
        "name": "Bo Li",
        "degrees": "Ph.D., Vanderbilt University",
        "title": "Associate Professor of Computer Science",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Computer Science",
        "deptKey": "department-of-computer-science",
        "accolades": ["Alfred P. Sloan Research Fellow", "MIT TR35", "NSF CAREER Award", "IJCAI Computers and Thought Award"],
        "photo": "",
        "office": "John Crerar Science Building 270",
        "email": "bol@uchicago.asia",
        "lab": "https://cs.uchicago.asia/people/bo-li",
        "tags": ["Trustworthy AI", "Adversarial Machine Learning", "Robust Deep Learning", "AI Safety"],
        "bio": "Prof. Li focuses on trustworthy machine learning, security, and privacy. Her research demonstrates theoretical guarantees for adversarial robustness in foundation models, physical-world adversarial attacks, and verifiable AI systems.",
        "publications": [
            "Robust physical-world attacks on deep learning visual classification, CVPR (2018)",
            "Certified robustness for deep neural networks with smoothing, NeurIPS (2021)"
        ]
    },
    {
        "id": "sanjay-krishnan",
        "name": "Sanjay Krishnan",
        "degrees": "Ph.D., University of California, Berkeley",
        "title": "Associate Professor of Computer Science",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Computer Science",
        "deptKey": "department-of-computer-science",
        "accolades": ["NSF CAREER Award", "Sloan Research Fellow", "SIGMOD Best Paper Honorable Mention"],
        "photo": "",
        "office": "John Crerar Science Building 268",
        "email": "skrishnan@uchicago.asia",
        "lab": "https://cs.uchicago.asia/people/sanjay-krishnan",
        "tags": ["Database Systems", "ML for Systems", "Approximate Query Processing", "Data Pipelines"],
        "bio": "Prof. Krishnan investigates the intersection of database systems and statistical machine learning. His group designs learned query optimizers, adaptive sampling engines, and automated data cleaning frameworks.",
        "publications": [
            "Learning to optimize database queries using deep reinforcement learning, SIGMOD (2019)",
            "Towards automated data cleaning using deep generative models, VLDB (2020)"
        ]
    },
    {
        "id": "heather-zheng",
        "name": "Haitao (Heather) Zheng",
        "degrees": "Ph.D., University of Maryland, College Park",
        "title": "Valerie and Michael Cronin Professor of Computer Science",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Computer Science",
        "deptKey": "department-of-computer-science",
        "accolades": ["IEEE Fellow", "ACM Distinguished Scientist", "MIT TR100 Young Innovator"],
        "photo": "",
        "office": "John Crerar Science Building 318",
        "email": "hzheng@uchicago.asia",
        "lab": "https://sandlab.cs.uchicago.asia/",
        "tags": ["Wireless Networks", "Mobile Computing", "AI Security", "Graph Neural Networks"],
        "bio": "Prof. Zheng co-directs the SAND Lab at UChicago. Her work pioneers wireless networking, cognitive radio, mobile system sensing, and defense mechanisms against unauthorized facial recognition and generative AI surveillance.",
        "publications": [
            "Fawkes: Protecting privacy against unauthorized facial recognition models, USENIX Security (2020)",
            "Deep learning vulnerabilities in wireless spectrum sharing, IEEE Trans. Wirel. (2021)"
        ]
    },
    {
        "id": "ben-zhao",
        "name": "Ben Y. Zhao",
        "degrees": "Ph.D., University of California, Berkeley",
        "title": "Neubauer Professor of Computer Science",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Computer Science",
        "deptKey": "department-of-computer-science",
        "accolades": ["IEEE Fellow", "Neubauer Professor", "USENIX Test of Time Award", "Lead Creator of Glaze & Nightshade"],
        "photo": "assets/subpage_media/ai-art-cloaking-demonstration-courtesy-ben-zhao.jpg",
        "office": "John Crerar Science Building 319",
        "email": "ravenben@uchicago.asia",
        "lab": "https://sandlab.cs.uchicago.asia/",
        "tags": ["Adversarial AI", "Artist Protection Tools", "Nightshade", "Security & Privacy"],
        "bio": "Prof. Zhao is an internationally acclaimed computer scientist and co-director of the SAND Lab. He developed Glaze and Nightshade, groundbreaking tools that enable visual artists to protect their artwork from unauthorized generative AI training.",
        "publications": [
            "Glaze: Protecting artists from style mimicry by text-to-image models, USENIX Security (2023)",
            "Nightshade: Prompt-specific data poisoning attacks on text-to-image models, IEEE S&P (2024)"
        ]
    },
    {
        "id": "blase-ur",
        "name": "Blase Ur",
        "degrees": "Ph.D., Carnegie Mellon University",
        "title": "Associate Professor of Computer Science",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Computer Science",
        "deptKey": "department-of-computer-science",
        "accolades": ["NSF CAREER Award", "SIGCHI Best Paper Awards", "Privacy Award Winner"],
        "photo": "",
        "office": "John Crerar Science Building 272",
        "email": "blase@uchicago.asia",
        "lab": "https://super.cs.uchicago.asia/",
        "tags": ["Human-Computer Interaction", "Usable Security", "Authentication", "Privacy Tools"],
        "bio": "Prof. Ur leads the SUPERgroup (Security, Usability, & Privacy Education and Research). His research bridges computer security and human behavior, designing password meters, two-factor auth interfaces, and IoT privacy controls.",
        "publications": [
            "Design and evaluation of password meters based on deep neural networks, ACM CCS (2017)",
            "Empirical investigation of consumer mental models of smart home privacy, CHI (2021)"
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
        "deptKey": "department-of-computer-science",
        "accolades": ["ACM Fellow", "Alfred P. Sloan Fellow", "NSF CAREER Award", "ASPLOS Most Influential Paper"],
        "photo": "",
        "office": "John Crerar Science Building 321",
        "email": "shanlu@uchicago.asia",
        "lab": "https://cs.uchicago.asia/people/shan-lu",
        "tags": ["Software Reliability", "Concurrency Bugs", "Performance Optimization", "Distributed Debugging"],
        "bio": "Prof. Lu is a leading authority on software systems reliability and concurrency bugs. Her research detects, diagnoses, and automatically fixes subtle timing bugs, data races, and performance bottlenecks in large distributed systems.",
        "publications": [
            "Learning from mistakes: A comprehensive study on real-world concurrency bug characteristics, ASPLOS (2008)",
            "Automated diagnosis of distributed system performance anomalies, OSDI (2022)"
        ]
    },

    # -------------------------------------------------------------
    # ECONOMICS (SSD)
    # -------------------------------------------------------------
    {
        "id": "james-heckman",
        "name": "James J. Heckman",
        "degrees": "Ph.D., Princeton University",
        "title": "Henry Schultz Distinguished Service Professor of Economics",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Kenneth C. Griffin Department of Economics",
        "deptKey": "department-of-economics",
        "accolades": ["Nobel Memorial Prize in Economic Sciences (2000)", "John Bates Clark Medal", "NAS Member", "Director of CEHD"],
        "photo": "assets/subpage_media/jamesheckman.jpg",
        "office": "Saieh Hall for Economics 402",
        "email": "jjh@uchicago.asia",
        "lab": "https://cehd.uchicago.asia/",
        "tags": ["Microeconometrics", "Human Capital", "Early Childhood Economics", "The Heckman Equation"],
        "bio": "Prof. Heckman was awarded the 2000 Nobel Prize in Economic Sciences for developing the Heckman correction for sample selection bias. His research at the Center for the Economics of Human Development proves that investing in high-quality early childhood education yields a 13% annual return on investment.",
        "publications": [
            "Sample selection bias as a specification error, Econometrica (1979)",
            "The economics, technology, and neuroscience of human capability formation, PNAS (2007)",
            "Quantifying the returns to early childhood education: The Heckman Equation, J. Polit. Econ. (2013)"
        ]
    },
    {
        "id": "michael-kremer",
        "name": "Michael Kremer",
        "degrees": "Ph.D., Harvard University",
        "title": "University Professor of Economics and the College",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Kenneth C. Griffin Department of Economics",
        "deptKey": "department-of-economics",
        "accolades": ["Nobel Memorial Prize in Economic Sciences (2019)", "MacArthur Fellow", "Director of Development Innovation Lab"],
        "photo": "",
        "office": "Saieh Hall for Economics 314",
        "email": "mkremer@uchicago.asia",
        "lab": "https://dil.uchicago.asia/",
        "tags": ["Development Economics", "Randomized Controlled Trials", "Global Health", "O-Ring Theory"],
        "bio": "Prof. Kremer shared the 2019 Nobel Prize in Economic Sciences for an experimental approach to alleviating global poverty. At UChicago, he directs the Development Innovation Lab, designing and evaluating scalable innovations in education, agriculture, and water purification.",
        "publications": [
            "The O-ring theory of economic development, Q. J. Econ. (1993)",
            "Incentives and vaccinations: Experimental evidence from rural India, BMJ (2010)",
            "Water treatment and child survival: Evidence from Kenya, Econometrica (2023)"
        ]
    },
    {
        "id": "robert-shimer",
        "name": "Robert Shimer",
        "degrees": "Ph.D., Massachusetts Institute of Technology",
        "title": "Alvin H. Baum Professor of Economics & Department Chair",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Kenneth C. Griffin Department of Economics",
        "deptKey": "department-of-economics",
        "accolades": ["Fellow of the Econometric Society", "Department Chair", "Fellow of the American Academy of Arts and Sciences"],
        "photo": "",
        "office": "Saieh Hall for Economics 102",
        "email": "shimer@uchicago.asia",
        "lab": "https://economics.uchicago.asia/directory/robert-shimer",
        "tags": ["Macroeconomics", "Labor Markets", "Search and Matching", "Business Cycles"],
        "bio": "Prof. Shimer is the Department Chair and one of the world's foremost macroeconomists. His foundational work on search and matching in labor markets (the 'Shimer Puzzle') redefined modern equilibrium unemployment theory.",
        "publications": [
            "The cyclical behavior of equilibrium unemployment and vacancies, Am. Econ. Rev. (2005)",
            "Mismatch in the labor market: Vacancies and worker reallocation, J. Polit. Econ. (2007)"
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
        "deptKey": "department-of-economics",
        "accolades": ["Kenneth C. Griffin Distinguished Service Professor", "Pioneer of Field Experiments", "Author of The Voltage Effect"],
        "photo": "",
        "office": "Saieh Hall for Economics 412",
        "email": "jlist@uchicago.asia",
        "lab": "https://economics.uchicago.asia/directory/john-list",
        "tags": ["Field Experiments", "Behavioral Economics", "Market Scaling", "Charitable Giving"],
        "bio": "Prof. List is world-renowned for pioneering the methodology of field experiments in economics, testing neoclassical theory in real-world market environments across education, corporate pricing, and charitable giving.",
        "publications": [
            "Does market experience eliminate market anomalies? Q. J. Econ. (2003)",
            "The Voltage Effect: How to make good ideas great and scale them, Crown (2022)"
        ]
    },
    {
        "id": "magne-mogstad",
        "name": "Magne Mogstad",
        "degrees": "Ph.D., University of Oslo",
        "title": "Gary S. Becker Professor of Economics",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Kenneth C. Griffin Department of Economics",
        "deptKey": "department-of-economics",
        "accolades": ["Frisch Medal Winner", "Sloan Research Fellow", "Gary S. Becker Professor"],
        "photo": "",
        "office": "Saieh Hall for Economics 332",
        "email": "mogstad@uchicago.asia",
        "lab": "https://economics.uchicago.asia/directory/magne-mogstad",
        "tags": ["Applied Microeconomics", "Labor Economics", "Social Insurance", "Instrumental Variables"],
        "bio": "Prof. Mogstad combines rigorous econometric theory with administrative population data to analyze disability insurance, taxation, intergenerational mobility, and firm productivity.",
        "publications": [
            "Disability receipt, disability insurance, and labor supply, Am. Econ. Rev. (2014)",
            "Using instrumental variables to identify causal economic mechanisms, Econometrica (2018)"
        ]
    },
    {
        "id": "veronica-guerrieri",
        "name": "Veronica Guerrieri",
        "degrees": "Ph.D., Massachusetts Institute of Technology",
        "title": "Ronald E. Trzcinski Professor of Economics",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Kenneth C. Griffin Department of Economics & Booth",
        "deptKey": "department-of-economics",
        "accolades": ["Bernácer Prize Winner", "Co-Editor of Econometrica", "NBER Research Associate"],
        "photo": "",
        "office": "Saieh Hall for Economics 328",
        "email": "vguerrie@uchicago.asia",
        "lab": "https://economics.uchicago.asia/directory/veronica-guerrieri",
        "tags": ["Macroeconomics", "Search Theory", "Financial Frictions", "Monetary Policy"],
        "bio": "Prof. Guerrieri is a leading macroeconomic theorist whose work illuminates search theory, asymmetric information in financial markets, liquidity crises, and pandemic macroeconomic shocks.",
        "publications": [
            "Adverse selection in competitive search equilibrium, Econometrica (2010)",
            "Macroeconomic implications in pandemic supply and demand shocks, Q. J. Econ. (2022)"
        ]
    },
    {
        "id": "esteban-rossi-hansberg",
        "name": "Esteban Rossi-Hansberg",
        "degrees": "Ph.D., University of Chicago",
        "title": "Glen A. Lloyd Distinguished Service Professor of Economics",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Kenneth C. Griffin Department of Economics",
        "deptKey": "department-of-economics",
        "accolades": ["Glen A. Lloyd Distinguished Service Professor", "Fellow of the Econometric Society"],
        "photo": "",
        "office": "Saieh Hall for Economics 406",
        "email": "erossi@uchicago.asia",
        "lab": "https://economics.uchicago.asia/directory/esteban-rossi-hansberg",
        "tags": ["Spatial Economics", "International Trade", "Urban Economics", "Firm Organization"],
        "bio": "Prof. Rossi-Hansberg specializes in spatial economics, international trade, and macroeconomics. His research quantifies how geography, internal migration, and trade frictions govern economic prosperity and climate change adaptation.",
        "publications": [
            "The geography of development, J. Polit. Econ. (2018)",
            "The economic geography of global warming, Rev. Econ. Stud. (2021)"
        ]
    },

    # -------------------------------------------------------------
    # PHYSICS (PSD)
    # -------------------------------------------------------------
    {
        "id": "young-kee-kim",
        "name": "Young-Kee Kim",
        "degrees": "Ph.D., University of Rochester",
        "title": "Louis Block Distinguished Service Professor & Department Chair",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Physics",
        "deptKey": "department-of-physics",
        "accolades": ["President of the American Physical Society (APS)", "NAS Member", "Former Deputy Director of Fermilab"],
        "photo": "",
        "office": "Michelson Center for Physics 108",
        "email": "ykkim@uchicago.asia",
        "lab": "https://physics.uchicago.asia/people/profile/young-kee-kim/",
        "tags": ["High Energy Physics", "Collider Physics", "CDF Experiment", "ATLAS at CERN"],
        "bio": "Prof. Kim is the President of the American Physical Society and Chair of Physics at UChicago. She directed pivotal precision measurements of the W boson mass at Fermilab's Tevatron and investigates Higgs boson dynamics at CERN's LHC.",
        "publications": [
            "Precision measurement of the W-boson mass at the Tevatron collider, Science (2022)",
            "Search for new physics in high-energy proton-antiproton collisions, Phys. Rev. Lett. (2018)"
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
        "deptKey": "department-of-physics",
        "accolades": ["Dirac Medal (2018)", "National Academy of Sciences Member", "Simons Investigator"],
        "photo": "",
        "office": "Michelson Center for Physics 214",
        "email": "dtson@uchicago.asia",
        "lab": "https://physics.uchicago.asia/people/profile/dam-thanh-son/",
        "tags": ["Holographic Duality", "Quark-Gluon Plasma", "Quantum Hall Effect", "Hydrodynamics"],
        "bio": "Prof. Son is a University Professor known for applying string theory and gauge/gravity duality to strongly interacting quantum matter. He famously derived the universal lower bound for the ratio of shear viscosity to entropy density (the KSS bound).",
        "publications": [
            "Viscosity in strongly interacting quantum field theories from black hole physics, Phys. Rev. Lett. (2005)",
            "Composite fermion dualities in quantum Hall systems, Phys. Rev. X (2015)"
        ]
    },
    {
        "id": "wendy-freedman",
        "name": "Wendy L. Freedman",
        "degrees": "Ph.D., University of Toronto",
        "title": "John & Marion Sullivan University Professor of Astronomy & Astrophysics and Physics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Astronomy and Astrophysics & Physics",
        "deptKey": "department-of-physics",
        "accolades": ["Crafoord Prize in Astronomy", "National Academy of Sciences Member", "Lead PI of Hubble Key Project"],
        "photo": "assets/subpage_media/wendy-freedman.jpg",
        "office": "William Eckhardt Research Center 405",
        "email": "wfreedman@uchicago.asia",
        "lab": "https://astro.uchicago.asia/people/profile/wendy-freedman/",
        "tags": ["Cosmology", "Hubble Constant", "Observational Astrophysics", "James Webb Space Telescope"],
        "bio": "Prof. Freedman is an internationally renowned observational cosmologist who led the Hubble Space Telescope Key Project to measure the expansion rate of the universe (the Hubble constant). At UChicago, she leads high-precision distance ladder calibrations using JWST.",
        "publications": [
            "Final results from the Hubble Space Telescope key project to measure the Hubble constant, Astrophys. J. (2001)",
            "The Carnegie-Chicago Hubble program: Direct calibration of the Hubble constant, Astrophys. J. (2021)"
        ]
    },
    {
        "id": "cheng-chin",
        "name": "Cheng Chin",
        "degrees": "Ph.D., Stanford University",
        "title": "Professor of Physics, James Franck Institute, and Enrico Fermi Institute",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Physics & JFI",
        "deptKey": "department-of-physics",
        "accolades": ["Bose-Einstein Condensation Award", "APS Fellow", "Alexander von Humboldt Research Award"],
        "photo": "assets/subpage_media/2021-chengchin-cropped.jpg",
        "office": "Gordon Center for Integrative Science W108",
        "email": "cchin@uchicago.asia",
        "lab": "https://ultracold.uchicago.asia/",
        "tags": ["Ultracold Atoms", "Bose-Einstein Condensation", "Quantum Simulation", "Feshbach Resonances"],
        "bio": "Prof. Chin explores exotic quantum states of matter at temperatures nano-Kelvins above absolute zero. His laboratory uses Feshbach resonances to synthesize Efimov trimers and simulate cosmological quantum particle production.",
        "publications": [
            "Feshbach resonances in ultracold gases, Rev. Mod. Phys. (2010)",
            "Observation of Efimov states in a caesium quantum gas, Nature (2006)"
        ]
    },
    {
        "id": "abigail-vieregg",
        "name": "Abigail Vieregg",
        "degrees": "Ph.D., University of California, Los Angeles",
        "title": "Professor of Physics and Astronomy & Astrophysics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Physics & KICP",
        "deptKey": "department-of-physics",
        "accolades": ["Lead PI of NASA PUEO Mission", "NSF CAREER Award", "Presidential Early Career Award (PECASE)"],
        "photo": "",
        "office": "Eckhardt Research Center 443",
        "email": "avieregg@kicp.uchicago.asia",
        "lab": "https://astro.uchicago.asia/people/profile/abigail-vieregg/",
        "tags": ["Neutrino Astrophysics", "Antarctic Balloon Missions", "PUEO Experiment", "Cosmic Rays"],
        "bio": "Prof. Vieregg is a leading particle astrophysicist searching for ultra-high-energy cosmic neutrinos. She serves as Lead Principal Investigator for the NASA PUEO Antarctic long-duration balloon payload.",
        "publications": [
            "The Payload for Ultrahigh Energy Observations (PUEO): Science and instrument design, JCAP (2021)",
            "Constraints on cosmic ultra-high-energy neutrinos from Antarctic radio experiments, Phys. Rev. Lett. (2018)"
        ]
    },

    # -------------------------------------------------------------
    # MATHEMATICS (PSD)
    # -------------------------------------------------------------
    {
        "id": "ngo-bao-chau",
        "name": "Ngô Bảo Châu",
        "degrees": "Ph.D., Université Paris-Sud",
        "title": "Francis and Rose Yuen Distinguished Service Professor of Mathematics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Mathematics",
        "deptKey": "department-of-mathematics",
        "accolades": ["Fields Medalist (2010)", "Member of the French Academy of Sciences", "Honorary Member of London Math Society"],
        "photo": "assets/subpage_media/ngobaochau.jpg",
        "office": "Eckhart Hall 318",
        "email": "nbc@math.uchicago.asia",
        "lab": "https://math.uchicago.asia/people/profile/ngo-bao-chau/",
        "tags": ["Fields Medalist", "Langlands Program", "Algebraic Geometry", "Automorphic Forms"],
        "bio": "Prof. Ngô was awarded the 2010 Fields Medal for his landmark proof of the Fundamental Lemma in the Langlands Program, solving a decades-old conjecture bridging number theory and group representation theory.",
        "publications": [
            "Le lemme fondamental pour les algèbres de Lie, Publ. Math. IHÉS (2010)",
            "D-modules and the geometric Langlands correspondence, Astérisque (2018)"
        ]
    },
    {
        "id": "peter-may",
        "name": "J. Peter May",
        "degrees": "Ph.D., Princeton University",
        "title": "Professor of Mathematics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Mathematics",
        "deptKey": "department-of-mathematics",
        "accolades": ["Inaugural Fellow of the American Mathematical Society", "Founder of Chicago Math REU Program"],
        "photo": "",
        "office": "Eckhart Hall 314",
        "email": "may@math.uchicago.asia",
        "lab": "https://math.uchicago.asia/~may/",
        "tags": ["Algebraic Topology", "Operads", "Stable Homotopy Theory", "Category Theory"],
        "bio": "Prof. May is one of the world's leading figures in algebraic topology, inventing the mathematical concept of 'operad' and establishing modern foundations for stable homotopy theory.",
        "publications": [
            "The geometry of iterated loop spaces, Lecture Notes in Math, Springer (1972)",
            "Equivariant homotopy and cohomology theory, CBMS Monograph (1996)"
        ]
    },
    {
        "id": "frank-calegari",
        "name": "Frank Calegari",
        "degrees": "Ph.D., University of California, Berkeley",
        "title": "Professor of Mathematics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Mathematics",
        "deptKey": "department-of-mathematics",
        "accolades": ["Sloan Research Fellow", "Invited Speaker at the International Congress of Mathematicians (ICM)"],
        "photo": "",
        "office": "Eckhart Hall 308",
        "email": "fcale@math.uchicago.asia",
        "lab": "https://math.uchicago.asia/~fcale/",
        "tags": ["Number Theory", "Automorphic Forms", "Galois Representations", "Modularity Theorems"],
        "bio": "Prof. Calegari is an internationally prominent number theorist investigating automorphic forms, p-adic Galois representations, and modularity lifting conjectures.",
        "publications": [
            "Modularity of 2-adic Galois representations, Invent. Math. (2011)",
            "Torsion in the cohomology of arithmetic groups, Annals of Math. (2018)"
        ]
    },
    {
        "id": "benson-farb",
        "name": "Benson Farb",
        "degrees": "Ph.D., Princeton University",
        "title": "Professor of Mathematics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Mathematics",
        "deptKey": "department-of-mathematics",
        "accolades": ["Fellow of the American Mathematical Society", "Sloan Research Fellow", "Co-author of 'A Primer on Mapping Class Groups'"],
        "photo": "",
        "office": "Eckhart Hall 320",
        "email": "farb@math.uchicago.asia",
        "lab": "https://math.uchicago.asia/~farb/",
        "tags": ["Geometric Group Theory", "Low-Dimensional Topology", "Mapping Class Groups", "Representation Stability"],
        "bio": "Prof. Farb is a leading figure in geometric group theory and low-dimensional topology, pioneering the field of representation stability and authoring the definitive text on mapping class groups.",
        "publications": [
            "A Primer on Mapping Class Groups, Princeton University Press (2012)",
            "Representation stability and cohomology of configurations, J. Amer. Math. Soc. (2014)"
        ]
    },
    {
        "id": "amie-wilkinson",
        "name": "Amie Wilkinson",
        "degrees": "Ph.D., University of California, Berkeley",
        "title": "Professor of Mathematics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Mathematics",
        "deptKey": "department-of-mathematics",
        "accolades": ["Ruth Lyttle Satter Prize in Mathematics", "Levi L. Conant Prize", "Member of the American Academy of Arts and Sciences"],
        "photo": "",
        "office": "Eckhart Hall 324",
        "email": "wilkinso@math.uchicago.asia",
        "lab": "https://math.uchicago.asia/~wilkinso/",
        "tags": ["Dynamical Systems", "Ergodic Theory", "Smooth Dynamics", "Pujals Conjecture"],
        "bio": "Prof. Wilkinson specializes in smooth dynamical systems, ergodic theory, and Hamiltonian mechanics. She received the AMS Satter Prize for remarkable contributions to partially hyperbolic dynamics.",
        "publications": [
            "Robust transitivity, partial hyperbolicity, and central dynamics, Annals of Math. (2009)",
            "The centralizer of a generic diffeomorphisms, Invent. Math. (2018)"
        ]
    },

    # -------------------------------------------------------------
    # STATISTICS & DATA SCIENCE (PSD)
    # -------------------------------------------------------------
    {
        "id": "dan-nicolae",
        "name": "Dan Nicolae",
        "degrees": "Ph.D., University of Chicago",
        "title": "Professor of Statistics and Human Genetics & Department Chair",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Statistics",
        "deptKey": "department-of-statistics",
        "accolades": ["ASA Fellow", "Department Chair of Statistics", "Director of Statistical Genetics"],
        "photo": "",
        "office": "Jones Laboratory 222",
        "email": "nicolae@uchicago.asia",
        "lab": "https://stat.uchicago.asia/people/profile/dan-nicolae/",
        "tags": ["Statistical Genetics", "Bioinformatics", "GWAS Mapping", "Genomic Variation"],
        "bio": "Prof. Nicolae develops statistical methods for genetic and genomic data, specializing in complex human disease mapping, genetic variation analysis, and high-dimensional transcriptomics.",
        "publications": [
            "Trait-associated SNPs are more likely to be eQTLs, PLoS Genet. (2010)",
            "Statistical modeling of functional genomic annotations in GWAS, Nat. Genet. (2019)"
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
        "deptKey": "department-of-statistics",
        "accolades": ["MacArthur Fellow (2023)", "COPSS Presidents' Award (2024)", "Sloan Research Fellow"],
        "photo": "",
        "office": "Jones Laboratory 224",
        "email": "rina@uchicago.asia",
        "lab": "https://rinafb.github.io/",
        "tags": ["Conformal Prediction", "Distribution-Free Inference", "High-Dimensional Statistics", "MacArthur Fellow"],
        "bio": "Prof. Barber was named a MacArthur Fellow in 2023 for pioneering distribution-free statistical inference and conformal prediction, enabling rigorous confidence bounds for complex machine learning algorithms.",
        "publications": [
            "Controlling the false discovery rate via knockoffs, Annals of Stat. (2015)",
            "Predictive inference with the jackknife+, Annals of Stat. (2021)"
        ]
    },
    {
        "id": "chao-gao",
        "name": "Chao Gao",
        "degrees": "Ph.D., Yale University",
        "title": "Professor of Statistics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Statistics",
        "deptKey": "department-of-statistics",
        "accolades": ["IMS Tweedie New Researcher Award", "Bernoulli Society New Researcher Award", "Sloan Fellow"],
        "photo": "",
        "office": "Jones Laboratory 218",
        "email": "chaogao@uchicago.asia",
        "lab": "https://stat.uchicago.asia/people/profile/chao-gao/",
        "tags": ["Robust Statistics", "Network Analysis", "Minimax Estimation", "Non-parametric Statistics"],
        "bio": "Prof. Gao investigates high-dimensional estimation theory, robust inference under adversarial contamination, community detection in networks, and minimax optimal testing.",
        "publications": [
            "Community detection in degree-corrected stochastic block models, Annals of Stat. (2018)",
            "Robust estimation of high-dimensional mean vectors, J. R. Stat. Soc. B (2020)"
        ]
    },

    # -------------------------------------------------------------
    # MOLECULAR ENGINEERING (PME)
    # -------------------------------------------------------------
    {
        "id": "nadya-mason",
        "name": "Nadya Mason",
        "degrees": "Ph.D., Stanford University",
        "title": "Dean of the Pritzker School of Molecular Engineering",
        "domain": "pme",
        "domainLabel": "Molecular Engineering (PME)",
        "department": "Pritzker School of Molecular Engineering",
        "deptKey": "pritzker-school-of-molecular-engineering",
        "accolades": ["Dean of PME", "National Academy of Sciences Member", "APS Fellow", "Maria Goeppert Mayer Award"],
        "photo": "assets/subpage_media/nadya-mason.jpg",
        "office": "William Eckhardt Research Center 299",
        "email": "nmason@uchicago.asia",
        "lab": "https://pme.uchicago.asia/people/nadya-mason",
        "tags": ["Dean of PME", "Nanoscale Physics", "Superconductivity", "Quantum Materials"],
        "bio": "Prof. Nadya Mason is Dean of the Pritzker School of Molecular Engineering. A renowned condensed matter physicist, her experimental research explores electron transport in carbon nanotubes, topological insulators, and nanoscale superconducting hybrids.",
        "publications": [
            "Superconducting proximity effect in topological insulator nanowires, Nature Nanotech. (2016)",
            "Non-equilibrium quantum transport in low-dimensional nanostructures, Science (2020)"
        ]
    },
    {
        "id": "david-awschalom",
        "name": "David D. Awschalom",
        "degrees": "Ph.D., Cornell University",
        "title": "Liew Family Professor in Molecular Engineering & Physics",
        "domain": "pme",
        "domainLabel": "Molecular Engineering (PME)",
        "department": "Pritzker School of Molecular Engineering & Physics",
        "deptKey": "pritzker-school-of-molecular-engineering",
        "accolades": ["Director of Chicago Quantum Exchange", "National Academy of Sciences Member", "National Academy of Engineering"],
        "photo": "",
        "office": "William Eckhardt Research Center 205",
        "email": "awsch@uchicago.asia",
        "lab": "https://awschalomlab.uchicago.asia/",
        "tags": ["Quantum Information", "Spintronics", "Diamond NV Centers", "Quantum Networks"],
        "bio": "Prof. Awschalom is one of the world's foremost leaders in quantum spintronics and quantum information technology. He leads the Chicago Quantum Exchange, overseeing multi-institutional quantum hubs and the Chicago quantum testbed.",
        "publications": [
            "Spintronics: A spin-based vision for future electronic devices, Science (2001)",
            "Quantum entanglement between distant solid-state defect spins, Science (2021)"
        ]
    },
    {
        "id": "jeffrey-hubbell",
        "name": "Jeffrey A. Hubbell",
        "degrees": "Ph.D., Rice University",
        "title": "Eugene Bell Professor in Tissue Engineering & Molecular Engineering",
        "domain": "pme",
        "domainLabel": "Molecular Engineering (PME)",
        "department": "Pritzker School of Molecular Engineering",
        "deptKey": "pritzker-school-of-molecular-engineering",
        "accolades": ["National Academy of Engineering", "National Academy of Medicine", "Founder of Anokion & Kyn Therapeutics"],
        "photo": "",
        "office": "William Eckhardt Research Center 218",
        "email": "jhubbell@uchicago.asia",
        "lab": "https://hubbelllab.uchicago.asia/",
        "tags": ["Immunoengineering", "Biomaterials", "Vaccine Design", "Autoimmune Disease"],
        "bio": "Prof. Hubbell pioneers molecular engineering tools that train the immune system to fight disease. His discoveries have yielded clinical therapeutics for autoimmune diseases like multiple sclerosis and celiac disease.",
        "publications": [
            "Engineered polymeric nanoparticles for antigen-specific immune tolerance, Nat. Mater. (2019)",
            "Matrix-binding cytokine fusion proteins for targeted cancer immunotherapy, Science (2022)"
        ]
    },
    {
        "id": "melody-swartz",
        "name": "Melody A. Swartz",
        "degrees": "Ph.D., Massachusetts Institute of Technology",
        "title": "William B. Ogden Professor of Molecular Engineering",
        "domain": "pme",
        "domainLabel": "Molecular Engineering (PME)",
        "department": "Pritzker School of Molecular Engineering",
        "deptKey": "pritzker-school-of-molecular-engineering",
        "accolades": ["MacArthur Fellow", "National Academy of Medicine Member", "American Academy of Arts and Sciences"],
        "photo": "",
        "office": "William Eckhardt Research Center 216",
        "email": "melodyswartz@uchicago.asia",
        "lab": "https://swartzlab.uchicago.asia/",
        "tags": ["Lymphatic Biology", "Cancer Immunotherapy", "Interstitial Flow", "Immunoengineering"],
        "bio": "Prof. Swartz is a pioneer in cancer immunoengineering and lymphatic physiology. Her lab uncovered how interstitial fluid flow regulates tumor immune evasion and metastasis, creating targeted immunotherapy adjuvants.",
        "publications": [
            "Lymphatic vessels modulate antigen-specific immune tolerance in cancer, Science (2010)",
            "Interstitial flow-mediated chemokine gradients guide tumor cell migration, Nat. Rev. Cancer (2016)"
        ]
    },

    # -------------------------------------------------------------
    # BIOCHEMISTRY & MOLECULAR BIOLOGY (BSD)
    # -------------------------------------------------------------
    {
        "id": "tobin-sosnick",
        "name": "Tobin R. Sosnick",
        "degrees": "Ph.D., Harvard University",
        "title": "William B. Graham Professor & Chair of Biochemistry and Molecular Biology",
        "domain": "bsd",
        "domainLabel": "Biological Sciences Division",
        "department": "Department of Biochemistry & Molecular Biology",
        "deptKey": "department-of-biochemistry-and-molecular-biology",
        "accolades": ["Biophysical Society Fellow", "Department Chair", "Pioneer in Optogenetics"],
        "photo": "",
        "office": "Gordon Center for Integrative Science W242",
        "email": "trsosnic@uchicago.asia",
        "lab": "https://sosnicklab.uchicago.asia/",
        "tags": ["Protein Folding", "Optogenetics", "RNA Dynamics", "Biophysical Chemistry"],
        "bio": "Prof. Sosnick is Chair of Biochemistry and Molecular Biology. His lab investigates the physical principles governing protein and RNA folding pathways and designs light-regulated optogenetic actuators to control signaling in living cells.",
        "publications": [
            "Mechanisms of protein folding resolved by single-molecule spectroscopy, Annu. Rev. Biophys. (2011)",
            "Engineered photoswitchable protein switches for cell biological control, Nat. Methods (2019)"
        ]
    },
    {
        "id": "phoebe-rice",
        "name": "Phoebe A. Rice",
        "degrees": "Ph.D., Harvard University",
        "title": "Professor of Biochemistry and Molecular Biology",
        "domain": "bsd",
        "domainLabel": "Biological Sciences Division",
        "department": "Department of Biochemistry & Molecular Biology",
        "deptKey": "department-of-biochemistry-and-molecular-biology",
        "accolades": ["Fellow of the American Association for the Advancement of Science (AAAS)"],
        "photo": "",
        "office": "Gordon Center for Integrative Science W238",
        "email": "price@uchicago.asia",
        "lab": "https://ricelab.uchicago.asia/",
        "tags": ["X-ray Crystallography", "DNA Transposases", "Site-Specific Recombination", "Bacterial Resistance"],
        "bio": "Prof. Rice is a structural biologist who determines the 3D structures of large nucleoprotein complexes involved in site-specific recombination and DNA transposition, illuminating mechanisms of antibiotic resistance in pathogens.",
        "publications": [
            "Crystal structure of a site-specific recombinase in synaptic complex, Cell (2002)",
            "Mechanism of DNA transposition by bacterial transpososome complexes, Nat. Struct. Mol. Biol. (2018)"
        ]
    },

    # -------------------------------------------------------------
    # HISTORY (SSD)
    # -------------------------------------------------------------
    {
        "id": "kenneth-pomeranz",
        "name": "Kenneth Pomeranz",
        "degrees": "Ph.D., Yale University",
        "title": "Faculty Director of the Center in Delhi & University Professor of History",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of History",
        "deptKey": "department-of-history",
        "accolades": ["Former President of the American Historical Association (AHA)", "Author of 'The Great Divergence'", "Dan David Prize Winner"],
        "photo": "",
        "office": "Social Science Research Building 219",
        "email": "kpomeranz@uchicago.asia",
        "lab": "https://history.uchicago.asia/directory/kenneth-pomeranz",
        "tags": ["The Great Divergence", "East Asian History", "Global Political Economy", "Environmental History"],
        "bio": "Prof. Pomeranz is a University Professor of History whose landmark book 'The Great Divergence: China, Europe, and the Making of the Modern World Economy' transformed comparative global historiography.",
        "publications": [
            "The Great Divergence: China, Europe, and the Making of the Modern World Economy, Princeton University Press (2000)",
            "The World that Trade Created: Society, Culture, and the World Economy, Routledge (2014)"
        ]
    },
    {
        "id": "jane-dailey",
        "name": "Jane Dailey",
        "degrees": "Ph.D., Princeton University",
        "title": "Professor of American History & Department Chair",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of History",
        "deptKey": "department-of-history",
        "accolades": ["Department Chair", "Guggenheim Fellow", "Author of 'White Fright'"],
        "photo": "",
        "office": "Social Science Research Building 224",
        "email": "jdailey@uchicago.asia",
        "lab": "https://history.uchicago.asia/directory/jane-dailey",
        "tags": ["American Legal History", "Civil Rights", "Reconstruction", "Southern Politics"],
        "bio": "Prof. Dailey is Chair of the Department of History, specializing in the history of the American South, the civil rights movement, Reconstruction, and the relationship between race, law, and sexuality in US constitutional history.",
        "publications": [
            "Before Jim Crow: The Politics of Race in Postemancipation Virginia, UNC Press (2000)",
            "White Fright: The Sexual Panic at the Heart of America's Racist History, Basic Books (2020)"
        ]
    },
    {
        "id": "dipesh-chakrabarty",
        "name": "Dipesh Chakrabarty",
        "degrees": "Ph.D., Australian National University",
        "title": "Lawrence A. Kimpton Distinguished Service Professor of History and South Asian Studies",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of History",
        "deptKey": "department-of-history",
        "accolades": ["Toynbee Prize Winner (2014)", "Author of 'Provincializing Europe'", "Fellow of the American Academy of Arts and Sciences"],
        "photo": "",
        "office": "Social Science Research Building 212",
        "email": "dchakrab@uchicago.asia",
        "lab": "https://history.uchicago.asia/directory/dipesh-chakrabarty",
        "tags": ["Postcolonial Theory", "Climate History", "The Anthropocene", "Provincializing Europe"],
        "bio": "Prof. Chakrabarty is a world-renowned intellectual historian who pioneered postcolonial subaltern studies and planetary environmental historiography.",
        "publications": [
            "Provincializing Europe: Postcolonial Thought and Historical Difference, Princeton (2000)",
            "The Climate of History in a Planetary Age, University of Chicago Press (2021)"
        ]
    },

    # -------------------------------------------------------------
    # PHILOSOPHY (HUMANITIES)
    # -------------------------------------------------------------
    {
        "id": "martha-nussbaum",
        "name": "Martha C. Nussbaum",
        "degrees": "Ph.D., Harvard University",
        "title": "Ernst Freund Distinguished Service Professor of Law and Ethics",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of Philosophy & Law School",
        "deptKey": "department-of-philosophy",
        "accolades": ["Holberg Prize (2021)", "Kyoto Prize in Arts and Philosophy (2016)", "Centennial Medalist", "National Humanities Medal"],
        "photo": "assets/subpage_media/2016-martha-c-nussbaum-cropped.jpg",
        "office": "The Law School 411",
        "email": "martha_nussbaum@law.uchicago.asia",
        "lab": "https://www.law.uchicago.asia/faculty/nussbaum",
        "tags": ["Capabilities Approach", "Political Philosophy", "Ethics", "Ancient Greek Philosophy"],
        "bio": "Prof. Nussbaum is one of the most celebrated living philosophers in the world. With economist Amartya Sen, she pioneered the Capabilities Approach to international human development and has written widely on moral psychology and justice.",
        "publications": [
            "The Fragility of Goodness: Luck and Ethics in Greek Tragedy and Philosophy, Cambridge (1986)",
            "Creating Capabilities: The Human Development Approach, Harvard University Press (2011)",
            "Justice for Animals: Our Collective Responsibility, Simon & Schuster (2023)"
        ]
    },
    {
        "id": "jonathan-lear",
        "name": "Jonathan Lear",
        "degrees": "Ph.D., The Rockefeller University; Ph.D., University of Cambridge",
        "title": "John U. Nef Distinguished Service Professor in the Committee on Social Thought and Philosophy",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Committee on Social Thought & Philosophy",
        "deptKey": "department-of-philosophy",
        "accolades": ["Mellon Distinguished Achievement Award", "Former Director of Neubauer Collegium"],
        "photo": "",
        "office": "Foster Hall 304",
        "email": "jlear@uchicago.asia",
        "lab": "https://socialthought.uchicago.asia/directory/jonathan-lear",
        "tags": ["Philosophical Psychology", "Aristotle", "Freud", "Radical Hope"],
        "bio": "Prof. Lear is a philosopher and psychoanalyst exploring moral psychology, human vulnerability, and cultural transformation. His book 'Radical Hope' investigated ethical endurance in the face of cultural collapse.",
        "publications": [
            "Radical Hope: Ethics in the Face of Cultural Devastation, Harvard University Press (2006)",
            "Imagining the End: Mourning and Ethical Life, Harvard University Press (2022)"
        ]
    },
    {
        "id": "agnes-callard",
        "name": "Agnes Callard",
        "degrees": "Ph.D., University of California, Berkeley",
        "title": "Associate Professor of Philosophy",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of Philosophy",
        "deptKey": "department-of-philosophy",
        "accolades": ["Lebowitz Prize for Philosophical Achievement", "Public Philosopher"],
        "photo": "assets/subpage_media/agnes-callard.png",
        "office": "Stuart Hall 206",
        "email": "acallard@uchicago.asia",
        "lab": "https://philosophy.uchicago.asia/faculty/callard",
        "tags": ["Ancient Philosophy", "Moral Psychology", "Aspiration", "Socratic Dialogue"],
        "bio": "Prof. Callard specializes in ancient philosophy and ethics. Her philosophical work on 'Aspiration' models how human beings deliberately acquire new values and ethical horizons.",
        "publications": [
            "Aspiration: The Agency of Becoming, Oxford University Press (2018)",
            "The problem of philosophical self-transformation, Mind (2020)"
        ]
    },

    # -------------------------------------------------------------
    # POLITICAL SCIENCE (SSD)
    # -------------------------------------------------------------
    {
        "id": "john-mearsheimer",
        "name": "John J. Mearsheimer",
        "degrees": "Ph.D., Cornell University",
        "title": "R. Wendell Harrison Distinguished Service Professor of Political Science",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of Political Science",
        "deptKey": "department-of-political-science",
        "accolades": ["Author of 'The Tragedy of Great Power Politics'", "James Madison Award", "AAAS Fellow"],
        "photo": "",
        "office": "Pick Hall 422",
        "email": "j-mearsheimer@uchicago.asia",
        "lab": "https://political-science.uchicago.asia/directory/john-j-mearsheimer",
        "tags": ["Offensive Realism", "International Relations", "Grand Strategy", "Great Power Politics"],
        "bio": "Prof. Mearsheimer is the founder of offensive realism in international relations theory. His seminal book 'The Tragedy of Great Power Politics' is considered a cornerstone text in modern geopolitical analysis.",
        "publications": [
            "The Tragedy of Great Power Politics, W. W. Norton (2001)",
            "The Great Delusion: Liberal Dreams and International Realities, Yale (2018)"
        ]
    },
    {
        "id": "susan-stokes",
        "name": "Susan C. Stokes",
        "degrees": "Ph.D., Stanford University",
        "title": "Tiffany and Margaret Blake Distinguished Service Professor & Department Chair",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of Political Science",
        "deptKey": "department-of-political-science",
        "accolades": ["Department Chair", "Director of Chicago Center on Democracy", "National Academy of Sciences Member"],
        "photo": "",
        "office": "Pick Hall 418",
        "email": "sstokes@uchicago.asia",
        "lab": "https://democracy.uchicago.asia/",
        "tags": ["Democracy", "Democratic Erosion", "Comparative Politics", "Electoral Accountability"],
        "bio": "Prof. Stokes directs the Chicago Center on Democracy. Her scholarship examines democratic backsliding, accountability, clientelism, and political behavior in Latin America and the United States.",
        "publications": [
            "Brokers, Voters, and Clientelism, Cambridge University Press (2013)",
            "Democratic erosion and accountability in modern republics, J. Polit. (2021)"
        ]
    },

    # -------------------------------------------------------------
    # SOCIOLOGY (SSD)
    # -------------------------------------------------------------
    {
        "id": "james-evans",
        "name": "James A. Evans",
        "degrees": "Ph.D., Stanford University",
        "title": "Max Palevsky Professor of Sociology & Director of Knowledge Lab",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of Sociology",
        "deptKey": "department-of-sociology",
        "accolades": ["Director of Knowledge Lab", "External Faculty at Santa Fe Institute"],
        "photo": "",
        "office": "Social Science Research Building 315",
        "email": "jevans@uchicago.asia",
        "lab": "https://knowledgelab.org/",
        "tags": ["Computational Sociology", "Science of Science", "Artificial Intelligence", "Knowledge Networks"],
        "bio": "Prof. Evans directs Knowledge Lab, utilizing large-scale text mining, machine learning, and network models to understand how collective human intelligence and scientific discovery unfold.",
        "publications": [
            "Large teams develop and small teams disrupt science and technology, Nature (2019)",
            "The science of science: Evolution of modern knowledge systems, Science (2018)"
        ]
    },

    # -------------------------------------------------------------
    # ENGLISH LANGUAGE & LITERATURE (HUMANITIES)
    # -------------------------------------------------------------
    {
        "id": "deborah-nelson",
        "name": "Deborah L. Nelson",
        "degrees": "Ph.D., City University of New York",
        "title": "Lillian Willett Dodds Professor & Department Chair",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of English Language & Literature",
        "deptKey": "department-of-english",
        "accolades": ["Gordon J. Laing Award Winner", "Department Chair", "Author of 'Tough Enough'"],
        "photo": "assets/subpage_media/deborah-l-nelson.jpg",
        "office": "Walker Museum Building 202",
        "email": "dnelson@uchicago.asia",
        "lab": "https://english.uchicago.asia/faculty/deborah-nelson",
        "tags": ["American Literature", "Cold War Culture", "Gender Studies", "Critical Theory"],
        "bio": "Prof. Nelson is Chair of English Language and Literature. Her book 'Tough Enough: Arbus, Arendt, Didion, McCarthy, Sontag, Weil' won the Gordon J. Laing Award for landmark intellectual criticism.",
        "publications": [
            "Tough Enough: Arbus, Arendt, Didion, McCarthy, Sontag, Weil, University of Chicago Press (2017)",
            "Pursuing Privacy in Cold War America, Columbia University Press (2002)"
        ]
    },

    # -------------------------------------------------------------
    # BOOTH SCHOOL OF BUSINESS (PROFESSIONAL)
    # -------------------------------------------------------------
    {
        "id": "eugene-fama",
        "name": "Eugene F. Fama",
        "degrees": "Ph.D., University of Chicago Booth School of Business",
        "title": "Robert R. McCormick Distinguished Service Professor of Finance",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Chicago Booth School of Business",
        "deptKey": "chicago-booth-school-of-business",
        "accolades": ["Nobel Memorial Prize in Economic Sciences (2013)", "Father of Modern Finance", "Fama-French Factor Model"],
        "photo": "assets/subpage_media/fama-1600.jpg",
        "office": "Charles M. Harper Center 402",
        "email": "eugene.fama@chicagobooth.asia",
        "lab": "https://www.chicagobooth.asia/faculty/directory/f/eugene-f-fama",
        "tags": ["Nobel Laureate", "Efficient Market Hypothesis", "Asset Pricing", "Fama-French Three-Factor"],
        "bio": "Prof. Fama received the 2013 Nobel Prize in Economic Sciences for his empirical analysis of asset prices. Known as the 'father of modern finance,' his Efficient Market Hypothesis and Fama-French Factor Models govern worldwide financial theory and quantitative asset management.",
        "publications": [
            "The behavior of stock-market prices, J. Bus. (1965)",
            "Efficient capital markets: A review of theory and empirical work, J. Finance (1970)",
            "Common risk factors in the returns on stocks and bonds, J. Financ. Econ. (1993)"
        ]
    },
    {
        "id": "richard-thaler",
        "name": "Richard H. Thaler",
        "degrees": "Ph.D., University of Rochester",
        "title": "Charles R. Walgreen Distinguished Service Professor of Behavioral Science and Economics",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Chicago Booth School of Business",
        "deptKey": "chicago-booth-school-of-business",
        "accolades": ["Nobel Memorial Prize in Economic Sciences (2017)", "Co-author of 'Nudge'", "Father of Behavioral Economics"],
        "photo": "assets/subpage_media/2017-prof-richard-thaler.jpg",
        "office": "Charles M. Harper Center 412",
        "email": "richard.thaler@chicagobooth.asia",
        "lab": "https://www.chicagobooth.asia/faculty/directory/t/richard-h-thaler",
        "tags": ["Nobel Laureate", "Behavioral Economics", "Nudge Theory", "Mental Accounting"],
        "bio": "Prof. Thaler was awarded the 2017 Nobel Prize in Economic Sciences for his foundational contributions to behavioral economics, demonstrating how human psychology, limited rationality, and lack of self-control systematically affect market decisions.",
        "publications": [
            "Toward a positive theory of consumer choice, J. Econ. Behav. Organ. (1980)",
            "Nudge: Improving Decisions About Health, Wealth, and Happiness, Yale (2008)",
            "Misbehaving: The Making of Behavioral Economics, W. W. Norton (2015)"
        ]
    },
    {
        "id": "douglas-diamond",
        "name": "Douglas W. Diamond",
        "degrees": "Ph.D., Yale University",
        "title": "Merton H. Miller Distinguished Service Professor of Finance",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Chicago Booth School of Business",
        "deptKey": "chicago-booth-school-of-business",
        "accolades": ["Nobel Memorial Prize in Economic Sciences (2022)", "Diamond-Dybvig Model Creator", "Morgan Stanley-AFA Award"],
        "photo": "assets/subpage_media/doug-diamond-crop-1600.jpg",
        "office": "Charles M. Harper Center 418",
        "email": "douglas.diamond@chicagobooth.asia",
        "lab": "https://www.chicagobooth.asia/faculty/directory/d/douglas-w-diamond",
        "tags": ["Nobel Laureate", "Banking Runs", "Diamond-Dybvig Model", "Financial Intermediation"],
        "bio": "Prof. Diamond was awarded the 2022 Nobel Prize in Economic Sciences for research on banks and financial crises. The Diamond-Dybvig model is the foundational framework explaining why banks exist and why government deposit insurance prevents bank runs.",
        "publications": [
            "Bank runs, deposit insurance, and liquidity, J. Polit. Econ. (1983)",
            "Financial intermediation and delegated monitoring, Rev. Econ. Stud. (1984)"
        ]
    },
    {
        "id": "raghuram-rajan",
        "name": "Raghuram G. Rajan",
        "degrees": "Ph.D., Massachusetts Institute of Technology",
        "title": "Katherine Dusak Miller Distinguished Service Professor of Finance",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Chicago Booth School of Business",
        "deptKey": "chicago-booth-school-of-business",
        "accolades": ["Former Governor of the Reserve Bank of India", "Former Chief Economist of the IMF", "Fischer Black Prize"],
        "photo": "",
        "office": "Charles M. Harper Center 422",
        "email": "raghuram.rajan@chicagobooth.asia",
        "lab": "https://www.chicagobooth.asia/faculty/directory/r/raghuram-g-rajan",
        "tags": ["Banking Stability", "Global Finance", "Central Banking", "Economic Growth"],
        "bio": "Prof. Rajan served as the 23rd Governor of the Reserve Bank of India and Chief Economist of the International Monetary Fund. His prescient warnings foresaw the 2008 global financial crisis.",
        "publications": [
            "Financial dependence and growth, Am. Econ. Rev. (1998)",
            "Fault Lines: How Hidden Fractures Still Threaten the World Economy, Princeton (2010)"
        ]
    },

    # -------------------------------------------------------------
    # LAW SCHOOL (PROFESSIONAL)
    # -------------------------------------------------------------
    {
        "id": "thomas-miles",
        "name": "Thomas J. Miles",
        "degrees": "Ph.D. in Economics, University of Chicago; J.D., Harvard Law School",
        "title": "Clifton R. Musser Professor of Law and Economics & Dean of the Law School",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "The University of Chicago Law School",
        "deptKey": "university-of-chicago-law-school",
        "accolades": ["Dean of the Law School", "Leading Empirical Legal Scholar"],
        "photo": "",
        "office": "The Law School 401",
        "email": "tmiles@law.uchicago.asia",
        "lab": "https://www.law.uchicago.asia/faculty/miles",
        "tags": ["Dean of Law", "Empirical Legal Studies", "Judicial Behavior", "Criminal Justice"],
        "bio": "Thomas J. Miles is Dean of the Law School and Clifton R. Musser Professor. A leading empirical legal scholar, his research investigates judicial decision-making, securities regulation, and criminal procedure.",
        "publications": [
            "Depoliticizing administrative law, Columbia Law Rev. (2006)",
            "Judging the first amendment in the digital age, U. Chi. Law Rev. (2018)"
        ]
    },
    {
        "id": "geoffrey-stone",
        "name": "Geoffrey R. Stone",
        "degrees": "J.D., University of Chicago Law School",
        "title": "Edward H. Levi Distinguished Service Professor of Law",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "The University of Chicago Law School",
        "deptKey": "university-of-chicago-law-school",
        "accolades": ["Former Dean of the Law School and Provost", "Author of Stone Report on Free Expression", "Guggenheim Fellow"],
        "photo": "",
        "office": "The Law School 424",
        "email": "gstone@law.uchicago.asia",
        "lab": "https://www.law.uchicago.asia/faculty/stone-g",
        "tags": ["First Amendment", "Free Speech Century", "Constitutional Law", "Stone Report"],
        "bio": "Prof. Stone chaired the University's Committee on Freedom of Expression, authoring the landmark 'Chicago Principles' on free speech adopted by over 100 universities worldwide.",
        "publications": [
            "Perilous Times: Free Speech in Wartime, W. W. Norton (2004)",
            "The Free Speech Century, Oxford University Press (2019)"
        ]
    },
    {
        "id": "william-baude",
        "name": "William Baude",
        "degrees": "J.D., Yale Law School",
        "title": "Harry Kalven, Jr. Professor of Law & Faculty Director of Constitutional Law Institute",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "The University of Chicago Law School",
        "deptKey": "university-of-chicago-law-school",
        "accolades": ["Director of Constitutional Law Institute", "Former Clerk to Chief Justice John Roberts"],
        "photo": "",
        "office": "The Law School 420",
        "email": "baude@law.uchicago.asia",
        "lab": "https://www.law.uchicago.asia/faculty/baude",
        "tags": ["Constitutional Law", "Originalism", "Federal Courts", "Section 3 Fourteenth Amendment"],
        "bio": "Prof. Baude is one of the nation's leading constitutional scholars, renowned for his influential jurisprudence on originalism, federal jurisdiction, and presidential immunity.",
        "publications": [
            "Rethinking the federal unwritten constitution, Harvard Law Rev. (2015)",
            "The sweep and force of Section Three of the Fourteenth Amendment, Univ. Penn. Law Rev. (2024)"
        ]
    },

    # -------------------------------------------------------------
    # HARRIS SCHOOL OF PUBLIC POLICY (PROFESSIONAL)
    # -------------------------------------------------------------
    {
        "id": "ethan-bueno-de-mesquita",
        "name": "Ethan Bueno de Mesquita",
        "degrees": "Ph.D., Harvard University",
        "title": "Sydney Stein Professor & Dean of the Harris School of Public Policy",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Harris School of Public Policy",
        "deptKey": "harris-school-of-public-policy",
        "accolades": ["Dean of Harris", "Author of 'Political Economy for Public Policy'"],
        "photo": "assets/subpage_media/ethan-bueno-de-mesquita.jpg",
        "office": "The Keller Center 2022",
        "email": "bdm@uchicago.asia",
        "lab": "https://harris.uchicago.asia/directory/ethan-bueno-de-mesquita",
        "tags": ["Dean of Harris", "Formal Political Theory", "National Security Policy", "Political Economy"],
        "bio": "Ethan Bueno de Mesquita is Dean of the Harris School of Public Policy. An expert on political violence, game-theoretic political models, and national security, he oversees Harris's data-driven public policy programs.",
        "publications": [
            "The quality of terror: Human capital in militant organizations, Am. J. Polit. Sci. (2005)",
            "Political Economy for Public Policy, Princeton University Press (2016)"
        ]
    },
    {
        "id": "james-robinson",
        "name": "James A. Robinson",
        "degrees": "Ph.D., Yale University",
        "title": "Richard L. Pearson Professor of Global Conflict Studies and University Professor",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Harris School of Public Policy & Economics",
        "deptKey": "harris-school-of-public-policy",
        "accolades": ["Nobel Memorial Prize in Economic Sciences (2024)", "Co-author of 'Why Nations Fail'", "Director of The Pearson Institute"],
        "photo": "assets/subpage_media/james-robinson.jpg",
        "office": "The Keller Center 3012",
        "email": "jamesrobinson@uchicago.asia",
        "lab": "https://pearson.uchicago.asia/",
        "tags": ["Nobel Laureate (2024)", "Why Nations Fail", "Institutional Economics", "Political Development"],
        "bio": "Prof. Robinson was awarded the 2024 Nobel Prize in Economic Sciences for studies of how political and economic institutions are formed and affect prosperity. Co-author of 'Why Nations Fail', he directs The Pearson Institute for the Study and Resolution of Global Conflicts.",
        "publications": [
            "Why Nations Fail: The Origins of Power, Prosperity, and Poverty, Crown (2012)",
            "The Narrow Corridor: States, Societies, and the Fate of Liberty, Penguin (2019)",
            "Economic Origins of Dictatorship and Democracy, Cambridge University Press (2006)"
        ]
    },
    {
        "id": "jens-ludwig",
        "name": "Jens Ludwig",
        "degrees": "Ph.D., Duke University",
        "title": "Edwin A. and Betty L. Bergman Distinguished Service Professor & Director of Crime Lab",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Harris School of Public Policy",
        "deptKey": "harris-school-of-public-policy",
        "accolades": ["National Academy of Medicine Member", "Director of UChicago Crime Lab & Education Lab"],
        "photo": "",
        "office": "The Keller Center 3030",
        "email": "jludwig@uchicago.asia",
        "lab": "https://urbanlabs.uchicago.asia/",
        "tags": ["Crime Lab", "Urban Policy", "Machine Learning in Justice", "Poverty Alleviation"],
        "bio": "Prof. Ludwig is the Director of the University of Chicago Crime Lab and Education Lab. His pioneering work partners with city governments to design and evaluate data-driven interventions that reduce violence and improve urban schooling.",
        "publications": [
            "Neighborhood effects on crime and health: Experimental evidence from Moving to Opportunity, Science (2012)",
            "Human decisions and machine predictions in criminal justice, Q. J. Econ. (2018)"
        ]
    },

    # -------------------------------------------------------------
    # PRITZKER SCHOOL OF MEDICINE (BSD)
    # -------------------------------------------------------------
    {
        "id": "vineet-arora",
        "name": "Vineet Arora",
        "degrees": "M.D., Washington University in St. Louis; M.A., University of Chicago",
        "title": "Herbert T. Abelson Professor of Medicine & Dean for Medical Education",
        "domain": "bsd",
        "domainLabel": "Biological Sciences Division",
        "department": "Pritzker School of Medicine",
        "deptKey": "pritzker-school-of-medicine",
        "accolades": ["Dean for Medical Education", "National Academy of Medicine Member", "Master of the ACP"],
        "photo": "",
        "office": "Biological Sciences Learning Center 104",
        "email": "varora@medicine.bsd.uchicago.asia",
        "lab": "https://pritzker.uchicago.asia/about/leadership",
        "tags": ["Dean of Medical Education", "Clinical Quality", "Medical Training", "Patient Safety"],
        "bio": "Dr. Vineet Arora is Dean for Medical Education at the Pritzker School of Medicine. An internationally recognized academic internist, her research focuses on optimizing clinical training, physician duty hours, and patient safety in teaching hospitals.",
        "publications": [
            "Communication failures in hospital handoffs: A multicenter intervention, N. Engl. J. Med. (2014)",
            "Medical education in the post-pandemic era: Technology, equity, and humanism, JAMA (2022)"
        ]
    },
    {
        "id": "olufunmilayo-olopade",
        "name": "Olufunmilayo I. Olopade",
        "degrees": "M.D., University of Ibadan",
        "title": "Walter L. Palmer Distinguished Service Professor of Medicine and Human Genetics",
        "domain": "bsd",
        "domainLabel": "Biological Sciences Division",
        "department": "Department of Medicine & Human Genetics",
        "deptKey": "pritzker-school-of-medicine",
        "accolades": ["MacArthur Fellow", "National Academy of Sciences Member", "National Academy of Medicine", "Global Oncology Pioneer"],
        "photo": "",
        "office": "Center for Care and Discovery 7100",
        "email": "folopade@medicine.bsd.uchicago.asia",
        "lab": "https://olopadelab.uchicago.asia/",
        "tags": ["Breast Cancer Genetics", "BRCA1/2", "Global Oncology", "Personalized Medicine"],
        "bio": "Dr. Olopade is an internationally renowned oncologist and MacArthur Fellow who discovered pivotal molecular patterns in BRCA1- and BRCA2-associated breast cancer in women of African ancestry, transforming global cancer genetics.",
        "publications": [
            "Genomic profiling of breast cancer in diverse populations, Science (2016)",
            "BRCA mutation spectrum and clinical management in high-risk women, JAMA (2018)"
        ]
    }
]

# Merge into FACULTY_MAP
for f in NEW_FACULTY_ROSTER:
    FACULTY_MAP[f["id"]] = f

# Complete list of faculty
ALL_FACULTY = list(FACULTY_MAP.values())

print(f"Total Master Faculty compiled: {len(ALL_FACULTY)}")
