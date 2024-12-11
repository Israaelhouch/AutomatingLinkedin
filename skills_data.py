
import pandas as pd
        
professional_skills = [
    "Leadership",
    "Communication",
    "Teamwork",
    "Problem-Solving",
    "Time Management",
    "Adaptability",
    "Critical Thinking",
    "Collaboration",
    "Negotiation",
    "Decision-Making",
    "Conflict Resolution",
    "Project Management",
    "Emotional Intelligence",
    "Work Ethic",
    "Active Listening"
]


technical_skills = [
    "Software Development",
    "Web Development",
    "Python",
    "JavaScript",
    "SQL",
    "Java",
    "Cloud Computing (AWS, Azure, Google Cloud)",
    "Cybersecurity",
    "Machine Learning",
    "Artificial Intelligence (AI)",
    "Data Analysis",
    "Database Management (SQL, NoSQL)",
    "DevOps",
    "Data Visualization (Tableau, Power BI)",
    "Git"
]
design_creative_skills = [
    "Graphic Design",
    "UI/UX Design",
    "Web Design",
    "Adobe Creative Suite (Photoshop, Illustrator, InDesign)",
    "Branding",
    "Illustration",
    "Motion Graphics",
    "3D Modeling",
    "Video Editing",
    "Typography",
    "Animation",
    "Photography",
    "Print Design",
    "Creative Direction",
    "Logo Design"
]
marketing_skills = [
    "Digital Marketing",
    "SEO (Search Engine Optimization)",
    "Content Marketing",
    "Social Media Marketing",
    "Email Marketing",
    "PPC (Pay-Per-Click)",
    "Brand Strategy",
    "Market Research",
    "Google Analytics",
    "Affiliate Marketing",
    "Marketing Automation",
    "Lead Generation",
    "Copywriting",
    "Campaign Management",
    "Customer Relationship Management (CRM)"
]
sales_skills = [
    "Sales Management",
    "B2B Sales",
    "B2C Sales",
    "Sales Strategy",
    "Negotiation",
    "Lead Generation",
    "Salesforce",
    "Account Management",
    "Customer Relationship Management (CRM)",
    "Sales Planning",
    "Prospecting",
    "Closing Deals",
    "Cold Calling",
    "Market Research",
    "Sales Presentations"
]
finance_accounting_skills = [
    "Financial Analysis",
    "Accounting (GAAP, IFRS)",
    "Budgeting",
    "Financial Reporting",
    "Tax Preparation",
    "Financial Modeling",
    "Investment Strategy",
    "Bookkeeping",
    "Cost Management",
    "Auditing",
    "Cash Flow Management",
    "Risk Management",
    "Payroll",
    "Mergers & Acquisitions (M&A)",
    "Corporate Finance"
]
project_management_skills = [
    "Project Planning",
    "Agile Methodology",
    "Scrum",
    "Risk Management",
    "Resource Management",
    "Project Scheduling",
    "Stakeholder Management",
    "Budget Management",
    "Quality Assurance (QA)",
    "Team Leadership",
    "Change Management",
    "Communication",
    "Problem Solving",
    "Project Coordination",
    "Timeline Management"
]
hr_recruitment_skills = [
    "Recruitment",
    "Talent Acquisition",
    "Employee Engagement",
    "Performance Management",
    "Organizational Development",
    "Conflict Resolution",
    "Workforce Planning",
    "Compensation & Benefits",
    "Labor Relations",
    "Onboarding",
    "Employee Relations",
    "HR Policies",
    "Diversity & Inclusion",
    "HRIS (Human Resource Information System)",
    "Training & Development"
]
customer_service_skills = [
    "Customer Service",
    "Conflict Resolution",
    "CRM Software (Salesforce, Zendesk)",
    "Technical Support",
    "Help Desk Operations",
    "Customer Satisfaction",
    "Troubleshooting",
    "Product Knowledge",
    "Active Listening",
    "Problem Solving",
    "Communication Skills",
    "Escalation Management",
    "Ticketing Systems",
    "Customer Retention",
    "Customer Support Training"
]
legal_skills = [
    "Contract Law",
    "Corporate Law",
    "Legal Research",
    "Litigation",
    "Compliance",
    "Intellectual Property (IP) Law",
    "Mergers & Acquisitions (M&A)",
    "Legal Writing",
    "Negotiation",
    "Dispute Resolution",
    "Employment Law",
    "Tax Law",
    "Real Estate Law",
    "Privacy Law",
    "Regulatory Affairs"
]
education_training_skills = [
    "Instructional Design",
    "Curriculum Development",
    "eLearning",
    "Training Delivery",
    "Coaching",
    "Mentorship",
    "Public Speaking",
    "Learning Management Systems (LMS)",
    "Needs Assessment",
    "Educational Technology",
    "Blended Learning",
    "Adult Education",
    "Facilitation",
    "Classroom Management",
    "Performance Evaluation"
]
languages_skills = [
    "English (Fluent, Native, Bilingual)",
    "Spanish",
    "French",
    "German",
    "Mandarin",
    "Arabic",
    "Portuguese",
    "Italian",
    "Russian",
    "Japanese",
    "Korean",
    "Hindi",
    "Dutch",
    "Swedish",
    "Turkish"
]
engineering_manufacturing_skills = [
    "Mechanical Engineering",
    "Electrical Engineering",
    "Civil Engineering",
    "Project Engineering",
    "CAD (AutoCAD, SolidWorks)",
    "Manufacturing Processes",
    "Quality Control",
    "Lean Manufacturing",
    "Process Improvement",
    "PLC Programming",
    "Product Design",
    "3D Modeling",
    "Industrial Engineering",
    "Supply Chain Management",
    "Operations Management"
]
science_healthcare_skills = [
    "Medical Research",
    "Clinical Research",
    "Pharmacology",
    "Biotechnology",
    "Laboratory Skills",
    "Healthcare Management",
    "Patient Care",
    "Medical Imaging",
    "Pharmaceuticals",
    "Nursing",
    "Public Health",
    "Health Education",
    "Regulatory Affairs",
    "Epidemiology",
    "Genetics"
]
it_networking_skills = [
    "Network Administration",
    "Cisco Networking (CCNA, CCNP)",
    "LAN/WAN Management",
    "Network Security",
    "Firewall Configuration",
    "VPN (Virtual Private Network)",
    "Cloud Computing (AWS, Azure, Google Cloud)",
    "Network Protocols (TCP/IP, DNS, HTTP)",
    "System Administration",
    "IT Support",
    "Virtualization (VMware, Hyper-V)",
    "Server Management",
    "Cybersecurity",
    "Linux/Unix",
    "Troubleshooting"
]
travel_planning_skills = [
    "Itinerary Planning",
    "Travel Coordination",
    "Flight Booking",
    "Hotel Reservations",
    "Group Travel Management",
    "Travel Budgeting",
    "Event Planning",
    "Destination Research",
    "Travel Documentation",
    "Visa & Passport Assistance",
    "Transportation Arrangements",
    "Client Service",
    "Travel Policies",
    "Risk Management",
    "Travel Consulting"
]
environmental_sustainability_skills = [
    "Sustainability Reporting",
    "Environmental Impact Assessment",
    "Renewable Energy",
    "Climate Change Mitigation",
    "Environmental Compliance",
    "Sustainable Development",
    "Waste Management",
    "Carbon Footprint Reduction",
    "Green Building Standards (LEED)",
    "Resource Conservation",
    "Environmental Policy",
    "Eco-friendly Product Design",
    "Water Management",
    "Sustainable Agriculture",
    "Energy Efficiency"
]

skills={"Professional Skills":professional_skills,
        "Technical Skills":technical_skills,
        "Design & Creative":design_creative_skills,
        "Marketing":marketing_skills,
        "Sales":sales_skills,
        "Finance & Accounting":finance_accounting_skills,
        "Project Management":project_management_skills,
        "Human Resources (HR) & Recruitment":hr_recruitment_skills,
        "Customer Service & Support": customer_service_skills,
        "Legal Skills":legal_skills,
        "Education & Training":education_training_skills,
        "Languages":languages_skills,
        "Engineering & Manufacturing":engineering_manufacturing_skills,
        "Science & Healthcare":science_healthcare_skills,
        "IT & Networking":it_networking_skills,
        "Travel planning":travel_planning_skills,
        "Environmental Sustainability":environmental_sustainability_skills}

skills_df=pd.DataFrame(skills)
skills_df.to_csv('skills.csv', index=False)


