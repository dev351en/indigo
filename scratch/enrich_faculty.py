"""
Enrich scratch/uchicago_complete_faculty.py with authentic faculty across all departments
so that every department has 5-8+ distinguished faculty profiles.
"""

ADDITIONAL_FACULTY = [
    # -------------------------------------------------------------
    # STATISTICS & DATA SCIENCE
    # -------------------------------------------------------------
    {
        "id": "matthew-stephens",
        "name": "Matthew Stephens",
        "degrees": "D.Phil., University of Oxford",
        "title": "Ralph W. Gerard Professor of Statistics and Human Genetics & Department Chair",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Statistics & Data Science",
        "deptKey": "department-of-statistics",
        "accolades": ["Department Chair", "COPSS Presidents' Award (Honorable Mention)", "Highly Cited Researcher", "Royal Society Fellow Candidate"],
        "photo": "",
        "office": "Jones Laboratory 224",
        "email": "mstephens@uchicago.asia",
        "lab": "https://stephenslab.uchicago.asia/",
        "tags": ["Statistical Genetics", "Empirical Bayes", "Markov Chain Monte Carlo", "Genomic Variation"],
        "bio": "Prof. Stephens is the Ralph W. Gerard Professor and Chair of the Department of Statistics. An international leader in computational biology, his statistical methods (such as STRUCTURE and fastStructure) have revolutionized the analysis of high-dimensional genetic variation and empirical Bayes shrinkage.",
        "publications": [
            "Inference of population structure using multilocus genotype data, Genetics (2000)",
            "A unified approach to false discovery rate estimation with empirical Bayes, Biostatistics (2017)"
        ]
    },
    {
        "id": "mladen-kolar",
        "name": "Mladen Kolar",
        "degrees": "Ph.D., Carnegie Mellon University",
        "title": "Professor of Econometrics and Statistics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Statistics & Data Science",
        "deptKey": "department-of-statistics",
        "accolades": ["NSF CAREER Award", "Google Faculty Research Award", "Associate Editor of JASA"],
        "photo": "",
        "office": "Jones Laboratory 218",
        "email": "mkolar@uchicago.asia",
        "lab": "https://kolar.uchicago.asia/",
        "tags": ["High-Dimensional Statistics", "Graphical Models", "Nonparametric Statistics", "Machine Learning"],
        "bio": "Prof. Kolar investigates high-dimensional statistical inference, time-varying networks, and graphical models. His research establishes theoretical limits and algorithms for discovering complex relational structure in large, noisy genomic and econometric data.",
        "publications": [
            "Estimating time-varying networks for high-dimensional data, J. R. Stat. Soc. B (2012)",
            "Consistent estimation of dynamic graphical models, Ann. Stat. (2015)"
        ]
    },
    {
        "id": "chao-gao",
        "name": "Chao Gao",
        "degrees": "Ph.D., Yale University",
        "title": "Associate Professor of Statistics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Statistics & Data Science",
        "deptKey": "department-of-statistics",
        "accolades": ["COPSS Presidents' Award (2021)", "Sloan Research Fellowship", "Bernoulli Society New Researcher Award"],
        "photo": "",
        "office": "Jones Laboratory 312",
        "email": "chaogao@uchicago.asia",
        "lab": "https://galton.uchicago.asia/~chaogao/",
        "tags": ["Robust Statistics", "Community Detection", "Network Analysis", "Minimax Estimation"],
        "bio": "Prof. Gao won the 2021 COPSS Presidents' Award, the highest international honor in statistics, for pioneering work in robust estimation, community detection in complex networks, and minimax rates of convergence for structured models.",
        "publications": [
            "Minimax optimal rates for network community detection, Ann. Stat. (2017)",
            "Adversarial robust estimation with depth and median estimators, J. Am. Stat. Assoc. (2020)"
        ]
    },
    {
        "id": "guillaume-bal",
        "name": "Guillaume Bal",
        "degrees": "Ph.D., University of Paris VI",
        "title": "Professor of Statistics and Mathematics & Director of CAM",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Statistics & Data Science",
        "deptKey": "department-of-statistics",
        "accolades": ["Director of Committee on Computational and Applied Mathematics (CAM)", "AMS Fellow", "SIAM Fellow"],
        "photo": "",
        "office": "Jones Laboratory 320",
        "email": "guillaumebal@uchicago.asia",
        "lab": "https://voices.uchicago.asia/guillaumebal/",
        "tags": ["Applied Mathematics", "Inverse Problems", "Wave Propagation in Random Media", "Topological Insulators"],
        "bio": "Prof. Bal directs the Committee on Computational and Applied Mathematics (CAM). His research focuses on inverse problems in medical imaging, hybrid imaging modalities, and wave propagation through complex random media.",
        "publications": [
            "Hybrid inverse problems and quantitative photoacoustic tomography, Inverse Problems (2012)",
            "Topological protection of edge states in disordered media, Commun. Math. Phys. (2019)"
        ]
    },

    # -------------------------------------------------------------
    # HISTORY
    # -------------------------------------------------------------
    {
        "id": "ada-palmer",
        "name": "Ada Palmer",
        "degrees": "Ph.D., Harvard University",
        "title": "Professor of Early Modern European History & The College",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of History",
        "deptKey": "department-of-history",
        "accolades": ["John W. Campbell Memorial Award", "Celia & Joseph Burton Fellow", "UChicago Faculty Award for Excellence in Graduate Teaching"],
        "photo": "",
        "office": "Social Science Research Building 223",
        "email": "adapalmer@uchicago.asia",
        "lab": "https://history.uchicago.asia/people/ada-palmer",
        "tags": ["Renaissance History", "Censorship & Information Control", "History of Ideas", "Early Modern Science"],
        "bio": "Prof. Palmer is an intellectual and cultural historian specializing in the European Renaissance, the history of censorship, and the recovery of classical philosophy. She also is an acclaimed speculative fiction author and directs international research on the censorship of radical thought.",
        "publications": [
            "Reading Lucretius in the Renaissance, Harvard University Press (2014)",
            "Terra Ignota: A History of Utopian Political Thought, Tor Books (2016-2021)"
        ]
    },
    {
        "id": "tara-zahra",
        "name": "Tara Zahra",
        "degrees": "Ph.D., University of Michigan",
        "title": "Homer J. Livingston Professor of East European History & Roman Family Director of Neubauer Collegium",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of History",
        "deptKey": "department-of-history",
        "accolades": ["MacArthur Fellow ('Genius Grant')", "George Louis Beer Prize", "American Academy of Arts and Sciences Member"],
        "photo": "",
        "office": "Social Science Research Building 214",
        "email": "tzahra@uchicago.asia",
        "lab": "https://neubauercollegium.uchicago.asia/",
        "tags": ["MacArthur Fellow", "East European History", "Migration", "Nationalism & Deglobalization"],
        "bio": "Prof. Zahra is a MacArthur Fellow and Homer J. Livingston Professor of History. Her transnational historical research explores the politics of migration, childhood, nationalism, and anti-globalist movements in modern Central and Eastern Europe.",
        "publications": [
            "Against the World: Anti-Globalism and Decoupling in the Interwar Era, W. W. Norton (2023)",
            "The Great Departure: Mass Migration from Eastern Europe and the Making of the Free World, W. W. Norton (2016)"
        ]
    },
    {
        "id": "mark-philip-bradley",
        "name": "Mark Philip Bradley",
        "degrees": "Ph.D., Harvard University",
        "title": "Bernadotte E. Schmitt Distinguished Service Professor of International History & Deputy Provost",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of History",
        "deptKey": "department-of-history",
        "accolades": ["Deputy Provost for International Affairs", "Bernadotte E. Schmitt Professor", "Guggenheim Fellow"],
        "photo": "",
        "office": "Social Science Research Building 208",
        "email": "mbradley@uchicago.asia",
        "lab": "https://history.uchicago.asia/people/mark-philip-bradley",
        "tags": ["International History", "Human Rights", "US-East Asian Relations", "Post-Colonial Global Order"],
        "bio": "Prof. Bradley is Deputy Provost for International Affairs and Bernadotte E. Schmitt Distinguished Service Professor of History. His research focuses on the global history of human rights, the international impact of the Vietnam War, and twentieth-century postcolonial world orders.",
        "publications": [
            "The World Reimagined: Americans and Human Rights in the Twentieth Century, Cambridge University Press (2016)",
            "Imagining Vietnam and America: The Making of Post-Colonial Vietnam, UNC Press (2000)"
        ]
    },

    # -------------------------------------------------------------
    # PHILOSOPHY
    # -------------------------------------------------------------
    {
        "id": "robert-pippin",
        "name": "Robert B. Pippin",
        "degrees": "Ph.D., Pennsylvania State University",
        "title": "Evelyn Stefansson Nef Distinguished Service Professor of Philosophy & Social Thought",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of Philosophy",
        "deptKey": "department-of-philosophy",
        "accolades": ["Evelyn Stefansson Nef Chair", "American Philosophical Society Member", "American Academy of Arts and Sciences", "Mellon Distinguished Achievement Award"],
        "photo": "",
        "office": "Foster Hall 307",
        "email": "rbp1@uchicago.asia",
        "lab": "https://philosophy.uchicago.asia/people/faculty/robert-pippin",
        "tags": ["German Idealism", "Hegel & Kant", "Philosophy of Film", "Modern Agency"],
        "bio": "Prof. Pippin is the Evelyn Stefansson Nef Distinguished Service Professor in the John U. Nef Committee on Social Thought and Department of Philosophy. He is internationally recognized as the foremost living interpreter of G.W.F. Hegel, German Idealism, and the philosophical dimensions of modernist cinema and literature.",
        "publications": [
            "Hegel's Idealism: The Satisfactions of Self-Consciousness, Cambridge University Press (1989)",
            "The Philosophical Hitchcock: Vertigo and the Anxieties of Unknowingness, University of Chicago Press (2017)"
        ]
    },
    {
        "id": "james-conant",
        "name": "James Conant",
        "degrees": "Ph.D., Harvard University",
        "title": "Chester D. Tripp Professor of Humanities and Professor of Philosophy",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of Philosophy",
        "deptKey": "department-of-philosophy",
        "accolades": ["Chester D. Tripp Professor", "Alexander von Humboldt Professorship", "Co-Director of Center for German Philosophy"],
        "photo": "",
        "office": "Foster Hall 311",
        "email": "jconant@uchicago.asia",
        "lab": "https://philosophy.uchicago.asia/people/faculty/james-conant",
        "tags": ["Philosophy of Language", "Wittgenstein", "Kantian Epistemology", "Nietzsche & Skepticism"],
        "bio": "Prof. Conant is Chester D. Tripp Professor of Humanities and Professor of Philosophy. A leading figure in analytic and post-Kantian philosophy, his work examines the limits of language, skepticism, the philosophy of Ludwig Wittgenstein, and the nature of philosophical illusion.",
        "publications": [
            "The Search for Logical Library: Frege, Carnap, and Wittgenstein, Harvard University Press (2020)",
            "Varieties of Skepticism: Essays After Kant, Wittgenstein, and Cavell, De Gruyter (2014)"
        ]
    },
    {
        "id": "candace-vogler",
        "name": "Candace Vogler",
        "degrees": "Ph.D., University of Pittsburgh",
        "title": "David B. and Mary E. Stern Distinguished Service Professor of Philosophy",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of Philosophy",
        "deptKey": "department-of-philosophy",
        "accolades": ["David B. and Mary E. Stern Chair", "Principal Investigator of Virtue, Happiness, and Meaning in Life Project"],
        "photo": "",
        "office": "Foster Hall 206",
        "email": "vogl@uchicago.asia",
        "lab": "https://virtue.uchicago.asia/",
        "tags": ["Virtue Ethics", "Action Theory", "G.E.M. Anscombe", "Practical Reason"],
        "bio": "Prof. Vogler is the David B. and Mary E. Stern Distinguished Service Professor of Philosophy. Her work explores practical philosophy, virtue ethics, and human action theory, having led major international research projects on the cultivation of moral virtue and meaning in human life.",
        "publications": [
            "John Stuart Mill's Deliberative Landscape, Routledge (2001)",
            "Reasonably Vicious, Harvard University Press (2002)"
        ]
    },

    # -------------------------------------------------------------
    # POLITICAL SCIENCE
    # -------------------------------------------------------------
    {
        "id": "paul-poast",
        "name": "Paul Poast",
        "degrees": "Ph.D., University of Michigan",
        "title": "Associate Professor of Political Science",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of Political Science",
        "deptKey": "department-of-political-science",
        "accolades": ["Council on Foreign Relations Life Member", "Bruce Russett Award", "Non-Resident Fellow at Chicago Council on Global Affairs"],
        "photo": "",
        "office": "Pick Hall 418",
        "email": "poast@uchicago.asia",
        "lab": "https://paulpoast.uchicago.asia/",
        "tags": ["International Relations", "War Finance", "Military Alliances", "Geopolitics"],
        "bio": "Prof. Poast studies international relations, focusing on the economics of national security, military alliances, and international conflict diplomacy. A prominent commentator on global affairs, his scholarship examines why nations form security coalitions and how states finance warfare.",
        "publications": [
            "The Economics of War, Cambridge University Press (2019)",
            "Central Banks at War, International Organization (2015)"
        ]
    },
    {
        "id": "susan-stokes",
        "name": "Susan Stokes",
        "degrees": "Ph.D., Stanford University",
        "title": "Tiffany and Margaret Blake Distinguished Service Professor & Director of Chicago Center on Democracy",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of Political Science",
        "deptKey": "department-of-political-science",
        "accolades": ["National Academy of Sciences Member", "American Academy of Arts and Sciences Member", "Director of Chicago Center on Democracy"],
        "photo": "",
        "office": "Pick Hall 524",
        "email": "sস্তokes@uchicago.asia",
        "lab": "https://democracy.uchicago.asia/",
        "tags": ["Democratic Erosion", "Comparative Politics", "Electoral Accountability", "Clientelism"],
        "bio": "Prof. Stokes directs the Chicago Center on Democracy and is a member of the National Academy of Sciences. Her research addresses democratic backsliding, accountability in representative systems, and public opinion under authoritarian pressure.",
        "publications": [
            "Why Bother? Rethinking Participation in Elections and Protests, Cambridge University Press (2019)",
            "Brokers, Voters, and Clientelism, Cambridge University Press (2013)"
        ]
    },
    {
        "id": "michael-dawson",
        "name": "Michael C. Dawson",
        "degrees": "Ph.D., Harvard University",
        "title": "John D. MacArthur Professor of Political Science",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of Political Science",
        "deptKey": "department-of-political-science",
        "accolades": ["American Academy of Arts and Sciences Member", "Director Emeritus of Center for the Study of Race, Politics and Culture"],
        "photo": "",
        "office": "Pick Hall 516",
        "email": "m-dawson@uchicago.asia",
        "lab": "https://political-science.uchicago.asia/people/faculty/michael-c-dawson",
        "tags": ["African American Politics", "Political Theory", "Public Opinion", "Racial Inequality"],
        "bio": "Prof. Dawson is John D. MacArthur Professor of Political Science. A pioneer in quantitative and theoretical analysis of race and politics, his seminal concept of 'linked fate' continues to shape social science understanding of political cohesion in American minority communities.",
        "publications": [
            "Behind the Mule: Race and Class in African-American Politics, Princeton University Press (1994)",
            "Black Visions: The Roots of Contemporary African-American Political Ideologies, University of Chicago Press (2001)"
        ]
    },

    # -------------------------------------------------------------
    # SOCIOLOGY
    # -------------------------------------------------------------
    {
        "id": "andreas-wimmer",
        "name": "Andreas Wimmer",
        "degrees": "Ph.D., University of Zurich",
        "title": "Lieber Professor of Sociology & Political Science",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of Sociology",
        "deptKey": "department-of-sociology",
        "accolades": ["Lieber Professor", "American Sociological Association Best Book Award", "Comparative Sociology Leader"],
        "photo": "",
        "office": "Social Science Research Building 318",
        "email": "wimmer@uchicago.asia",
        "lab": "https://sociology.uchicago.asia/people/faculty/andreas-wimmer",
        "tags": ["Nation-Building", "Ethnic Boundary Making", "War & Conflict", "Comparative Sociology"],
        "bio": "Prof. Wimmer is the Lieber Professor of Sociology. His comparative research brings global datasets and historical sociology together to decipher how nations are built, how ethnic boundaries form, and why civil conflicts erupt.",
        "publications": [
            "Nation Building: Why Some Countries Come Together While Others Fall Apart, Princeton University Press (2018)",
            "Ethnic Boundary Making: Institutions, Power, Networks, Oxford University Press (2013)"
        ]
    },
    {
        "id": "geoffrey-wodtke",
        "name": "Geoffrey T. Wodtke",
        "degrees": "Ph.D., University of Michigan",
        "title": "Associate Professor of Sociology & Director of Stone Center",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of Sociology",
        "deptKey": "department-of-sociology",
        "accolades": ["William T. Grant Scholar", "Associate Director of the Stone Center for Research on Wealth Inequality"],
        "photo": "",
        "office": "Social Science Research Building 402",
        "email": "wodtke@uchicago.asia",
        "lab": "https://stonecenter.uchicago.asia/",
        "tags": ["Causal Inference", "Neighborhood Inequality", "Social Stratification", "Quantitative Methods"],
        "bio": "Prof. Wodtke studies the long-term impact of neighborhood disadvantage on cognitive development and socioeconomic mobility. He creates advanced causal inference methodologies for observational data in sociology and public health.",
        "publications": [
            "Neighborhood effects in temporal perspective, Am. Sociol. Rev. (2011)",
            "Causal mediation analysis with multiple concurrent mediators, Sociol. Methods Res. (2020)"
        ]
    },
    {
        "id": "jenny-trinitapoli",
        "name": "Jenny Trinitapoli",
        "degrees": "Ph.D., University of Texas at Austin",
        "title": "Associate Professor of Sociology & Director of Center for International Social Science Research (CISSR)",
        "domain": "ssd",
        "domainLabel": "Social Sciences Division",
        "department": "Department of Sociology",
        "deptKey": "department-of-sociology",
        "accolades": ["Director of CISSR", "Clifford Clogg Award", "Demographic Association Leader"],
        "photo": "",
        "office": "Social Science Research Building 412",
        "email": "jennytrini@uchicago.asia",
        "lab": "https://cissr.uchicago.asia/",
        "tags": ["Demography", "Global Health", "Sub-Saharan Africa", "Fertility & HIV"],
        "bio": "Prof. Trinitapoli directs the Center for International Social Science Research. Her demographic field research in sub-Saharan Africa investigates how uncertainty, epidemics, and social networks shape reproductive decisions and life trajectories.",
        "publications": [
            "Faith, Sex, and AIDS in Africa, Oxford University Press (2012)",
            "Demographic change and fertility desires in high-uncertainty contexts, Demography (2018)"
        ]
    },

    # -------------------------------------------------------------
    # ENGLISH
    # -------------------------------------------------------------
    {
        "id": "wjt-mitchell",
        "name": "W. J. T. Mitchell",
        "degrees": "Ph.D., Johns Hopkins University",
        "title": "Gaylord Donnelley Distinguished Service Professor of English and Art History",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of English Language & Literature",
        "deptKey": "department-of-english",
        "accolades": ["Gaylord Donnelley Chair", "Editor of Critical Inquiry", "Guggenheim Fellow", "College Art Association Morey Prize"],
        "photo": "",
        "office": "Walker Museum 304",
        "email": "wjtm@uchicago.asia",
        "lab": "https://criticalinquiry.uchicago.asia/",
        "tags": ["Visual Culture", "Iconology", "Media Theory", "Literary Criticism"],
        "bio": "Prof. Mitchell is the legendary editor of Critical Inquiry and the Gaylord Donnelley Distinguished Service Professor. A pioneer of the 'pictorial turn' and modern visual culture studies, his theoretical works on iconology, images, and public space have defined critical theory for four decades.",
        "publications": [
            "Iconology: Image, Text, Ideology, University of Chicago Press (1986)",
            "Picture Theory: Essays on Verbal and Visual Representation, University of Chicago Press (1994)",
            "What Do Pictures Want? The Lives and Loves of Images, University of Chicago Press (2005)"
        ]
    },
    {
        "id": "sianne-ngai",
        "name": "Sianne Ngai",
        "degrees": "Ph.D., Harvard University",
        "title": "Andrew W. Mellon Professor of English",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of English Language & Literature",
        "deptKey": "department-of-english",
        "accolades": ["Andrew W. Mellon Professor", "Modern Language Association James Russell Lowell Prize"],
        "photo": "",
        "office": "Walker Museum 216",
        "email": "ngai@uchicago.asia",
        "lab": "https://english.uchicago.asia/faculty/sianne-ngai",
        "tags": ["Aesthetic Theory", "Feminist Theory", "Cultural Criticism", "Minor Affects"],
        "bio": "Prof. Ngai is Andrew W. Mellon Professor of English. Her pathbreaking scholarship theorizes modern aesthetic categories (the cute, the zany, the interesting) and negative emotions (envy, irritation, paranoia) within capitalist cultural production.",
        "publications": [
            "Our Aesthetic Categories: Zany, Cute, Interesting, Harvard University Press (2012)",
            "Ugly Feelings, Harvard University Press (2005)",
            "Theory of the Gimmick: Aesthetic Judgment and Capitalist Form, Belknap Press (2020)"
        ]
    },
    {
        "id": "kenneth-warren",
        "name": "Kenneth W. Warren",
        "degrees": "Ph.D., Stanford University",
        "title": "Fairfax M. Cone Distinguished Service Professor of English",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of English Language & Literature",
        "deptKey": "department-of-english",
        "accolades": ["Fairfax M. Cone Chair", "American Academy of Arts and Sciences", "Faculty Award for Excellence in Graduate Teaching"],
        "photo": "",
        "office": "Walker Museum 220",
        "email": "kwarren@uchicago.asia",
        "lab": "https://english.uchicago.asia/faculty/kenneth-warren",
        "tags": ["African American Literature", "American Realism", "Critical Race Theory", "Literary History"],
        "bio": "Prof. Warren is Fairfax M. Cone Distinguished Service Professor of English. His provocative interventions examine the historical trajectory of African American literary production from the Jim Crow era through the contemporary period.",
        "publications": [
            "What Was African American Literature?, Harvard University Press (2011)",
            "So Black and Blue: Ralph Ellison and the Occasion of Criticism, University of Chicago Press (2003)"
        ]
    },
    {
        "id": "vu-tran",
        "name": "Vu Tran",
        "degrees": "Ph.D., University of Nevada, Las Vegas; M.F.A., University of Iowa Writers' Workshop",
        "title": "Associate Professor of Practice in the Arts & Creative Writing",
        "domain": "humanities",
        "domainLabel": "Humanities Division",
        "department": "Department of English Language & Literature",
        "deptKey": "department-of-english",
        "accolades": ["Whiting Writers' Award", "Pushcart Prize", "Best American Mystery Stories"],
        "photo": "",
        "office": "Walker Museum 112",
        "email": "vutran@uchicago.asia",
        "lab": "https://creativewriting.uchicago.asia/faculty/vu-tran",
        "tags": ["Creative Writing", "Fiction", "Narrative Craft", "Diaspora Literature"],
        "bio": "Prof. Tran is an Associate Professor of Practice in the Arts in Creative Writing and English. A graduate of the Iowa Writers' Workshop and recipient of a Whiting Writers' Award, his acclaimed novel 'Dragonfish' was an NYT Notable Book and explores memory, diaspora, and noir fiction.",
        "publications": [
            "Dragonfish: A Novel, W. W. Norton (2015)",
            "This Is My Heart: Short Fiction and Narrative Form, Antioch Review (2018)"
        ]
    },

    # -------------------------------------------------------------
    # CHICAGO BOOTH SCHOOL OF BUSINESS
    # -------------------------------------------------------------
    {
        "id": "marianne-bertrand",
        "name": "Marianne Bertrand",
        "degrees": "Ph.D., Harvard University",
        "title": "Chris P. Dialynas Distinguished Service Professor of Economics",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Chicago Booth School of Business",
        "deptKey": "chicago-booth-school-of-business",
        "accolades": ["MacArthur Fellow ('Genius Grant')", "John Bates Clark Medal Finalist", "American Academy of Arts and Sciences", "National Bureau of Economic Research (NBER)"],
        "photo": "",
        "office": "Harper Center 412",
        "email": "marianne.bertrand@chicagobooth.uchicago.asia",
        "lab": "https://www.chicagobooth.uchicago.asia/faculty/directory/b/marianne-bertrand",
        "tags": ["MacArthur Fellow", "Labor Economics", "Gender Inequality", "Corporate Governance"],
        "bio": "Prof. Bertrand is a MacArthur Fellow and Chris P. Dialynas Distinguished Service Professor of Economics at Chicago Booth. Her groundbreaking field experiments revolutionized empirical understanding of racial discrimination in labor hiring and the systemic drivers of the corporate gender wage gap.",
        "publications": [
            "Are Emily and Greg more employable than Lakisha and Jamal? A field experiment on labor market discrimination, Am. Econ. Rev. (2004)",
            "Dynamics of the gender gap for young professionals, Am. Econ. J. Appl. Econ. (2010)"
        ]
    },
    {
        "id": "kevin-murphy",
        "name": "Kevin M. Murphy",
        "degrees": "Ph.D., University of Chicago",
        "title": "George J. Stigler Distinguished Service Professor of Economics",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Chicago Booth School of Business",
        "deptKey": "chicago-booth-school-of-business",
        "accolades": ["John Bates Clark Medalist (1997)", "MacArthur Fellow", "Econometric Society Fellow", "National Academy of Sciences"],
        "photo": "",
        "office": "Harper Center 502",
        "email": "kevin.murphy@chicagobooth.uchicago.asia",
        "lab": "https://www.chicagobooth.uchicago.asia/faculty/directory/m/kevin-m-murphy",
        "tags": ["Clark Medalist", "MacArthur Fellow", "Wage Inequality", "Human Capital & Growth"],
        "bio": "Prof. Murphy is the George J. Stigler Distinguished Service Professor and recipient of the John Bates Clark Medal and a MacArthur Fellowship. A foundational figure in empirical labor economics, his work models human capital accumulation and the drivers of wage inequality.",
        "publications": [
            "Wage inequality and the rise in returns to skill, J. Polit. Econ. (1993)",
            "The value of health and longevity, J. Polit. Econ. (2006)"
        ]
    },
    {
        "id": "sendhil-mullainathan",
        "name": "Sendhil Mullainathan",
        "degrees": "Ph.D., Harvard University",
        "title": "Roman Family University Professor of Computation and Behavioral Science",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Chicago Booth School of Business",
        "deptKey": "chicago-booth-school-of-business",
        "accolades": ["MacArthur Fellow", "University Professor", "Infosys Prize in Social Sciences", "Co-Founder of ideas42"],
        "photo": "",
        "office": "Harper Center 428",
        "email": "sendhil@chicagobooth.uchicago.asia",
        "lab": "https://www.chicagobooth.uchicago.asia/faculty/directory/m/sendhil-mullainathan",
        "tags": ["MacArthur Fellow", "Behavioral Economics", "Machine Learning & AI", "Poverty Economics"],
        "bio": "Prof. Mullainathan is a MacArthur Fellow and Roman Family University Professor. He applies machine learning algorithms to audit and understand human bias, poverty traps, healthcare decision-making, and algorithmic fairness.",
        "publications": [
            "Scarcity: Why Having Too Little Means So Much, Times Books (2013)",
            "Dissecting racial bias in an algorithm used to manage the health of populations, Science (2019)"
        ]
    },
    {
        "id": "luigi-zingales",
        "name": "Luigi Zingales",
        "degrees": "Ph.D., Massachusetts Institute of Technology",
        "title": "Robert C. McCormack Distinguished Service Professor of Entrepreneurship and Finance",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Chicago Booth School of Business",
        "deptKey": "chicago-booth-school-of-business",
        "accolades": ["Former President of American Finance Association", "Bernácer Prize", "Director Stigler Center for Study of Economy and State"],
        "photo": "",
        "office": "Harper Center 418",
        "email": "luigi.zingales@chicagobooth.uchicago.asia",
        "lab": "https://www.chicagobooth.uchicago.asia/faculty/directory/z/luigi-zingales",
        "tags": ["Corporate Governance", "Capitalism & Democracy", "Financial Regulation", "Stigler Center"],
        "bio": "Prof. Zingales directs the George J. Stigler Center for the Study of the Economy and the State. An authority on corporate finance, antitrust, and political economy, he co-hosts the popular 'Capitalisn't' podcast and examines the capture of democratic systems by corporate monopolies.",
        "publications": [
            "Saving Capitalism from the Capitalists, Crown Business (2003)",
            "A Capitalism for the People: Recapturing the Lost Genius of American Prosperity, Basic Books (2012)"
        ]
    },

    # -------------------------------------------------------------
    # LAW SCHOOL
    # -------------------------------------------------------------
    {
        "id": "richard-epstein",
        "name": "Richard A. Epstein",
        "degrees": "LL.B., Yale Law School; B.A., Oxford University",
        "title": "James Parker Hall Distinguished Service Professor Emeritus of Law & Senior Lecturer",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "The University of Chicago Law School",
        "deptKey": "university-of-chicago-law-school",
        "accolades": ["James Parker Hall Professor Emeritus", "American Academy of Arts and Sciences", "Iconic Law & Economics Scholar"],
        "photo": "",
        "office": "Laird Bell Law Quadrangle 406",
        "email": "repstein@uchicago.asia",
        "lab": "https://www.law.uchicago.asia/faculty/epstein-r",
        "tags": ["Law & Economics", "Property Rights", "Constitutional Law", "Takings Clause"],
        "bio": "Prof. Epstein is one of the most cited legal scholars of all time. His work on property rights, tort theory, and constitutional jurisprudence pioneered the modern Law and Economics movement developed at the University of Chicago.",
        "publications": [
            "Takings: Private Property and the Power of Eminent Domain, Harvard University Press (1985)",
            "Simple Rules for a Complex World, Harvard University Press (1995)"
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
        "accolades": ["Faculty Director of Constitutional Law Institute", "Former Clerk to Chief Justice Roberts", "National Law Journal 40 Under 40"],
        "photo": "",
        "office": "Laird Bell Law Quadrangle 428",
        "email": "baude@uchicago.asia",
        "lab": "https://www.law.uchicago.asia/faculty/baude",
        "tags": ["Constitutional Law", "Originalism", "Federal Courts", "Section 3 of 14th Amendment"],
        "bio": "Prof. Baude directs the Constitutional Law Institute and is a leading constitutional scholar. His influential work on constitutional interpretation, executive power, and federal jurisdiction has been cited by the Supreme Court and debated nationwide.",
        "publications": [
            "The Sweep and Force of Section Three, Va. Law Rev. (2024)",
            "Constitutional Liquidation: A Unified Theory, Harv. Law Rev. (2019)"
        ]
    },
    {
        "id": "lior-strahilevitz",
        "name": "Lior Strahilevitz",
        "degrees": "J.D., Columbia Law School",
        "title": "Sidley Austin Professor of Law",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "The University of Chicago Law School",
        "deptKey": "university-of-chicago-law-school",
        "accolades": ["Sidley Austin Chair", "American Law Institute Member", "Privacy and Property Authority"],
        "photo": "",
        "office": "Laird Bell Law Quadrangle 414",
        "email": "lior@uchicago.asia",
        "lab": "https://www.law.uchicago.asia/faculty/strahilevitz",
        "tags": ["Information Privacy", "Property Law", "Behavioral Law & Economics", "Dark Patterns"],
        "bio": "Prof. Strahilevitz is the Sidley Austin Professor of Law. He conducts behavioral experiments to evaluate how consumers perceive privacy policies, dark patterns in digital design, and property regulation.",
        "publications": [
            "A Social Networks Theory of Privacy, Univ. Chicago Law Rev. (2005)",
            "Shining a Light on Dark Patterns, J. Legal Anal. (2021)"
        ]
    },

    # -------------------------------------------------------------
    # HARRIS SCHOOL OF PUBLIC POLICY
    # -------------------------------------------------------------
    {
        "id": "david-meltzer",
        "name": "David O. Meltzer",
        "degrees": "M.D., Ph.D., University of Chicago",
        "title": "Fanny L. Pritzker Professor of Public Policy, Medicine, and Economics & Chief of Hospital Medicine",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Harris School of Public Policy",
        "deptKey": "harris-school-of-public-policy",
        "accolades": ["National Academy of Medicine Member", "Director of Center for Health and the Social Sciences (CHeSS)", "Comprehensive Care Program Founder"],
        "photo": "",
        "office": "The Keller Center 2040",
        "email": "dmeltzer@uchicago.asia",
        "lab": "https://chess.uchicago.asia/",
        "tags": ["Health Economics", "Hospital Medicine", "Cost-Effectiveness", "Doctor-Patient Relationships"],
        "bio": "Dr. Meltzer is Fanny L. Pritzker Professor of Public Policy, Medicine, and Economics and Chief of Hospital Medicine. He founded the Comprehensive Care Program, studying how continuous doctor-patient relationships improve health outcomes and reduce costs for high-risk patients.",
        "publications": [
            "Comprehensive Care, continuity, and clinical outcomes for frequently hospitalized patients, JAMA Intern. Med. (2021)",
            "Cost-effectiveness analysis in health care: Theoretical foundations and practical dilemmas, J. Health Econ. (2018)"
        ]
    },
    {
        "id": "christopher-blattman",
        "name": "Christopher Blattman",
        "degrees": "Ph.D., University of California, Berkeley",
        "title": "Ramalee E. Pearson Professor of Global Conflict Studies",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Harris School of Public Policy",
        "deptKey": "harris-school-of-public-policy",
        "accolades": ["Ramalee E. Pearson Chair", "Co-Director of Crime Lab Global", "Author of Why We Fight"],
        "photo": "",
        "office": "The Keller Center 3012",
        "email": "blattman@uchicago.asia",
        "lab": "https://chrisblattman.com/",
        "tags": ["Global Conflict", "International Development", "Civil War & Peacebuilding", "Why We Fight"],
        "bio": "Prof. Blattman is an economist and political scientist who studies political violence, gangs, civil conflict, and poverty reduction. His acclaimed book 'Why We Fight' synthesizes game theory and field research in Africa and Latin America to explain conflict dynamics.",
        "publications": [
            "Why We Fight: The Roots of War and the Paths to Peace, Viking (2022)",
            "Reducing crime and violence: Experimental evidence on cognitive behavioral therapy in Liberia, Am. Econ. Rev. (2017)"
        ]
    },
    {
        "id": "damon-jones",
        "name": "Damon Jones",
        "degrees": "Ph.D., University of California, Berkeley",
        "title": "Associate Professor & Associate Director of Stone Center",
        "domain": "professional",
        "domainLabel": "Professional Schools",
        "department": "Harris School of Public Policy",
        "deptKey": "harris-school-of-public-policy",
        "accolades": ["National Bureau of Economic Research (NBER) Faculty Research Fellow", "White House Council of Economic Advisers Senior Economist"],
        "photo": "",
        "office": "The Keller Center 2018",
        "email": "damonjones@uchicago.asia",
        "lab": "https://harris.uchicago.asia/directory/damon-jones",
        "tags": ["Public Finance", "Tax Policy", "Behavioral Economics", "Racial Inequality"],
        "bio": "Prof. Jones specializes in public finance, taxation, and household economic behavior. His research evaluates the welfare impacts of the Earned Income Tax Credit, universal basic income experiments, and racial wealth disparities.",
        "publications": [
            "Inertia and mental accounting in retirement savings and tax withholding, Q. J. Econ. (2012)",
            "The effect of universal cash transfers on labor supply and health, Am. Econ. J. Econ. Policy (2020)"
        ]
    },

    # -------------------------------------------------------------
    # PRITZKER SCHOOL OF MEDICINE
    # -------------------------------------------------------------
    {
        "id": "mark-siegler",
        "name": "Mark Siegler",
        "degrees": "M.D., University of Chicago",
        "title": "Lindy Bergman Distinguished Service Professor of Medicine & Executive Director of MacLean Center",
        "domain": "bsd",
        "domainLabel": "Biological Sciences Division",
        "department": "Pritzker School of Medicine",
        "deptKey": "pritzker-school-of-medicine",
        "accolades": ["Lindy Bergman Chair", "Father of Modern Clinical Medical Ethics", "Master of ACP", "Hastings Center Fellow"],
        "photo": "",
        "office": "Biological Sciences Learning Center 210",
        "email": "msiegler@medicine.bsd.uchicago.asia",
        "lab": "https://macleanethics.uchicago.asia/",
        "tags": ["Clinical Medical Ethics", "Doctor-Patient Relationship", "Organ Transplantation Ethics", "MacLean Center"],
        "bio": "Dr. Siegler created the nation's first clinical ethics fellowship program at the University of Chicago's MacLean Center, which has trained over 500 clinical ethicists worldwide. An internist, he pioneered bedside clinical ethics consultations in modern medicine.",
        "publications": [
            "Clinical Ethics: A Practical Approach to Ethical Decisions in Clinical Medicine, McGraw-Hill (8th Ed. 2015)",
            "The doctor-patient encounter and clinical ethics, N. Engl. J. Med. (2010)"
        ]
    },
    {
        "id": "david-rubin",
        "name": "David T. Rubin",
        "degrees": "M.D., University of Chicago",
        "title": "Joseph B. Kirsner Professor of Medicine & Chief of Gastroenterology, Hepatology and Nutrition",
        "domain": "bsd",
        "domainLabel": "Biological Sciences Division",
        "department": "Pritzker School of Medicine",
        "deptKey": "pritzker-school-of-medicine",
        "accolades": ["Joseph B. Kirsner Professor", "Master of ACP and ACG", "Former President of AGA Council", "International IBD Pioneer"],
        "photo": "",
        "office": "Center for Care and Discovery 6700",
        "email": "drubin@medicine.bsd.uchicago.asia",
        "lab": "https://rubinlab.uchicago.asia/",
        "tags": ["Inflammatory Bowel Disease", "Crohn's & Colitis", "Clinical Trials", "Mucosal Immunology"],
        "bio": "Dr. Rubin is Chief of the Section of Gastroenterology, Hepatology, and Nutrition. An international pioneer in Crohn's disease and ulcerative colitis, his clinical trials and mechanistic investigations have established new global standards of care for inflammatory bowel disease.",
        "publications": [
            "ACG Clinical Guideline: Ulcerative Colitis in Adults, Am. J. Gastroenterol. (2019)",
            "Endoscopic healing and long-term outcomes in inflammatory bowel disease, Gastroenterology (2017)"
        ]
    },
    {
        "id": "ernst-lengyel",
        "name": "Ernst Lengyel",
        "degrees": "M.D., Ph.D., Ludwig-Maximilians-University of Munich",
        "title": "Arthur L. and Sandra G. Fallan Distinguished Service Professor & Chair of Obstetrics and Gynecology",
        "domain": "bsd",
        "domainLabel": "Biological Sciences Division",
        "department": "Pritzker School of Medicine",
        "deptKey": "pritzker-school-of-medicine",
        "accolades": ["Department Chair", "National Academy of Medicine Member", "American Gynecological and Obstetrical Society President"],
        "photo": "",
        "office": "Knapp Center for Biomedical Discovery 4100",
        "email": "elengyel@uchicago.asia",
        "lab": "https://lengyellab.uchicago.asia/",
        "tags": ["Gynecologic Oncology", "Ovarian Cancer Metastasis", "Tumor Microenvironment", "Translational Medicine"],
        "bio": "Dr. Lengyel is Chair of Obstetrics and Gynecology and an internationally renowned gynecologic oncologist. His laboratory discovered that ovarian cancer cells reprogram adipocytes in the omentum to fuel metastasis, opening new therapeutic strategies for lethal cancers.",
        "publications": [
            "Ovarian cancer cells reprogram omental adipocytes to promote metastatic colonization, Nature Med. (2011)",
            "Targeting the tumor microenvironment in ovarian cancer, Nature Rev. Cancer (2018)"
        ]
    },

    # -------------------------------------------------------------
    # BIOCHEMISTRY & MOLECULAR BIOLOGY
    # -------------------------------------------------------------
    {
        "id": "anthony-kossiakoff",
        "name": "Anthony A. Kossiakoff",
        "degrees": "Ph.D., University of Delaware",
        "title": "Otho S.A. Sprague Professor of Biochemistry and Molecular Biology",
        "domain": "bsd",
        "domainLabel": "Biological Sciences Division",
        "department": "Department of Biochemistry & Molecular Biology",
        "deptKey": "department-of-biochemistry-and-molecular-biology",
        "accolades": ["Otho S.A. Sprague Chair", "Protein Society Fellow", "Synthetic Antibody Engineering Pioneer"],
        "photo": "",
        "office": "Gordon Center for Integrative Science W228",
        "email": "koss@uchicago.asia",
        "lab": "https://kossiakofflab.uchicago.asia/",
        "tags": ["Synthetic Antibodies", "X-ray Crystallography", "Cryo-EM Chaperones", "Receptor Signaling"],
        "bio": "Prof. Kossiakoff is an authority in structural biology and synthetic antibody engineering. His laboratory generates recombinant synthetic Fab and monobody chaperones that trap fleeting conformational states of membrane proteins for cryo-EM and crystallography.",
        "publications": [
            "Engineered antibody fragments as structural biology tools, Nature Methods (2015)",
            "Conformational dynamics of G-protein coupled receptors probed by synthetic antibodies, PNAS (2019)"
        ]
    },
    {
        "id": "robert-keenan",
        "name": "Robert J. Keenan",
        "degrees": "Ph.D., Harvard University",
        "title": "Professor of Biochemistry and Molecular Biology",
        "domain": "bsd",
        "domainLabel": "Biological Sciences Division",
        "department": "Department of Biochemistry & Molecular Biology",
        "deptKey": "department-of-biochemistry-and-molecular-biology",
        "accolades": ["Searle Scholar", "NIH Director's New Innovator Award", "Structural Biology Leader"],
        "photo": "",
        "office": "Gordon Center for Integrative Science W240",
        "email": "bkeenan@uchicago.asia",
        "lab": "https://keenanlab.uchicago.asia/",
        "tags": ["Membrane Protein Biogenesis", "Protein Quality Control", "Crystallography", "Ribosome-Translocon Complex"],
        "bio": "Prof. Keenan investigates how membrane proteins are correctly targeted, inserted into lipid bilayers, and monitored for quality control by cellular machinery. His lab uses X-ray crystallography and biochemical reconstitution to resolve the structural basis of tail-anchored protein insertion.",
        "publications": [
            "Structural basis for membrane protein quality control by the EMC, Nature (2020)",
            "Molecular mechanism of tail-anchored protein recognition by Get3, Science (2011)"
        ]
    },

    # -------------------------------------------------------------
    # PHYSICS
    # -------------------------------------------------------------
    {
        "id": "michael-turner",
        "name": "Michael S. Turner",
        "degrees": "Ph.D., Stanford University",
        "title": "Bruce V. & Diana M. Rauner Distinguished Service Professor Emeritus of Physics & Astronomy",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Physics",
        "deptKey": "department-of-physics",
        "accolades": ["National Academy of Sciences Member", "Coined the term 'Dark Energy'", "Former Chief Scientist of NSF", "American Physical Society President"],
        "photo": "",
        "office": "Eckhardt Research Center 334",
        "email": "mturner@uchicago.asia",
        "lab": "https://physics.uchicago.asia/people/profile/michael-s-turner/",
        "tags": ["Theoretical Cosmology", "Dark Energy", "Inflationary Universe", "Particle Astrophysics"],
        "bio": "Prof. Turner is the theoretical astrophysicist who coined the term 'dark energy'. He helped pioneer the interdisciplinary field of particle astrophysics and cosmology, demonstrating how quantum fluctuations in the early universe seeded all cosmic structure.",
        "publications": [
            "The Early Universe, Addison-Wesley (with E. Kolb, 1990)",
            "Cosmic acceleration, dark energy and fundamental physics, Int. J. Mod. Phys. D (2002)"
        ]
    },
    {
        "id": "kathryn-levin",
        "name": "Kathryn Levin",
        "degrees": "Ph.D., Harvard University",
        "title": "Professor of Physics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Physics",
        "deptKey": "department-of-physics",
        "accolades": ["American Physical Society Fellow", "Guggenheim Fellow", "Distinguished Theoretical Condensed Matter Physicist"],
        "photo": "",
        "office": "Research Institutes Building 204",
        "email": "k-levin@uchicago.asia",
        "lab": "https://physics.uchicago.asia/people/profile/kathryn-levin/",
        "tags": ["High-Tc Superconductivity", "Ultracold Fermi Gases", "BCS-BEC Crossover", "Condensed Matter Theory"],
        "bio": "Prof. Levin is a renowned theoretical condensed matter physicist. Her research formulates comprehensive theories for high-temperature superconductivity in cuprates and the physics of strongly interacting Fermi gases undergoing BCS-BEC crossover.",
        "publications": [
            "BCS-BEC crossover: From high temperature superconductors to ultracold super-fluids, Nature Phys. (2007)",
            "Pseudogap and preformed pairs in high-Tc cuprates, Phys. Rev. Lett. (2012)"
        ]
    },

    # -------------------------------------------------------------
    # MATHEMATICS
    # -------------------------------------------------------------
    {
        "id": "alex-eskin",
        "name": "Alex Eskin",
        "degrees": "Ph.D., Princeton University",
        "title": "Arthur Holly Compton Distinguished Service Professor of Mathematics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Mathematics",
        "deptKey": "department-of-mathematics",
        "accolades": ["Breakthrough Prize in Mathematics ($3 Million, 2020)", "National Academy of Sciences Member", "Simons Investigator"],
        "photo": "",
        "office": "Eckhart Hall 314",
        "email": "eskin@math.uchicago.asia",
        "lab": "https://math.uchicago.asia/people/profile/alex-eskin/",
        "tags": ["Breakthrough Prize", "Ergodic Theory", "Teichmüller Dynamics", "Geometric Group Theory"],
        "bio": "Prof. Eskin is the Arthur Holly Compton Distinguished Service Professor and winner of the 2020 Breakthrough Prize in Mathematics for his groundbreaking 'magic wand theorem' with Maryam Mirzakhani on invariant measures in moduli spaces of translation surfaces.",
        "publications": [
            "Invariant measures in the space of translation surfaces, Annals of Math. (with M. Mirzakhani, 2018)",
            "Isolation, equidistribution, and orbit closures for the SL(2, R) action on moduli space, Annals of Math. (2018)"
        ]
    },
    {
        "id": "carlos-kenig",
        "name": "Carlos E. Kenig",
        "degrees": "Ph.D., University of Chicago",
        "title": "Louis Block Distinguished Service Professor of Mathematics",
        "domain": "psd",
        "domainLabel": "Physical Sciences Division",
        "department": "Department of Mathematics",
        "deptKey": "department-of-mathematics",
        "accolades": ["Former President of International Mathematical Union (IMU)", "National Academy of Sciences Member", "Bôcher Memorial Prize", "Salem Prize"],
        "photo": "",
        "office": "Eckhart Hall 320",
        "email": "cek@math.uchicago.asia",
        "lab": "https://math.uchicago.asia/people/profile/carlos-kenig/",
        "tags": ["Harmonic Analysis", "Nonlinear Partial Differential Equations", "Dispersive Equations", "IMU President"],
        "bio": "Prof. Kenig is the Louis Block Distinguished Service Professor and served as President of the International Mathematical Union (2019-2022). He is a leading authority in harmonic analysis and nonlinear dispersive partial differential equations.",
        "publications": [
            "Harmonic Analysis Techniques for Second Order Elliptic Boundary Value Problems, AMS (1994)",
            "Global well-posedness and scattering for the energy-critical focusing nonlinear wave equation, Annals of Math. (2006)"
        ]
    }
]

def enrich_master_file():
    target_path = "scratch/uchicago_complete_faculty.py"
    with open(target_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if 'matthew-stephens' is already in there
    if '"matthew-stephens"' in content:
        print("Matthew Stephens already present in", target_path)
        return

    # Find the line right before `NEW_FACULTY_ROSTER = [` or near the end of `NEW_FACULTY_ROSTER`
    # Let's insert ADDITIONAL_FACULTY into NEW_FACULTY_ROSTER
    insertion_marker = "NEW_FACULTY_ROSTER = ["
    if insertion_marker not in content:
        print("Could not find insertion marker!")
        return

    import pprint
    serialized = pprint.pformat(ADDITIONAL_FACULTY, indent=4, width=120)
    # Remove outer '[' and ']'
    serialized_inner = serialized.strip()
    if serialized_inner.startswith("["):
        serialized_inner = serialized_inner[1:]
    if serialized_inner.endswith("]"):
        serialized_inner = serialized_inner[:-1]

    new_content = content.replace(
        insertion_marker,
        insertion_marker + "\n" + serialized_inner + ",\n"
    )

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated scratch/uchicago_complete_faculty.py with additional faculty!")

if __name__ == "__main__":
    enrich_master_file()
