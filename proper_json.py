import json

data = {
    "mode": "OFFLINE",
    "publishedOn": "2023-08-04",
    "refreshedOn": "2023-08-04",
    "source": "https://uniqusai-gpt-prod.s3.ap-south-1.amazonaws.com/big4/ey/Worldwide R&D Incentives Reference Guide 2022 _ EY - Global.pdf",
    "priority": 2,
    "content": "The main content of the text is about the EY Worldwide R&D Incentives Reference Guide for 2022. It mentions that the guide provides information on incentives available in 45 jurisdictions for companies looking to invest in R&D, innovation, and sustainability. Each chapter of the guide includes contact information for EY R&D incentive professionals, an overview of the country's approach to incentivizing R&D, and a checklist of available incentives. The guide also provides information on the benefits, application guidelines, eligibility requirements, and intellectual property and jurisdictional requirements for each incentive. It is important to note that the applicability of the incentives depends on the taxpayers' specific facts and circumstances. The text also briefly mentions that EY is a global leader in assurance, consulting, strategy and transactions, and tax services, and their services help build trust and confidence in the capital markets and economies worldwide.",
    "summary": "The Worldwide R&D Incentives Reference Guide provided by EY is a comprehensive resource for companies looking to leverage available incentives in various jurisdictions. The guide is particularly useful for those considering investments in research and development (R&D), innovation, and sustainability.\n \n The guide is structured in a straightforward manner, with each chapter focusing on a specific jurisdiction. It begins with contact information for key EY R&D incentive professionals, allowing users to easily reach out for further assistance.\n \n For each jurisdiction, the guide provides an overview of the country's approach to incentivizing R&D, innovation, or sustainability-related activities. It also includes a checklist of the types of incentives available, indicating which ones are applicable in that particular jurisdiction. In cases where incentives are commonly referred to in the local language, translations are provided for clarity.\n \n It is important to note that the applicability of incentives is dependent on the individual taxpayer's specific facts and circumstances. However, the guide does provide valuable insights by listing the benefits delivered by each incentive.\n \n In addition to the benefits provided, the guide also includes guidelines around incentive applications, eligibility requirements, and intellectual property and jurisdictional requirements. This information is crucial for companies to understand the necessary steps and criteria for accessing the incentives.\n \n Overall, the Worldwide R&D Incentives Reference Guide by EY is a valuable tool for companies seeking to maximize their opportunities for incentives in R&D, innovation, and sustainability. It offers a comprehensive and structured overview of incentives available across various jurisdictions, providing key information for companies to make informed decisions and potentially benefit from these incentives.",
    "tags": 'tax', 'R&D', 'incentives', 'sustainability', 'EY',
    "tagArr": ['tax', ' R&D', ' incentives', ' sustainability', ' EY'],
    "title": "Worldwide R&D Incentives Reference Guide 2022 _ EY - Global.pdf",
    "status": "active",
    "link": "https://uniqusai-gpt-prod.s3.ap-south-1.amazonaws.com/big4/ey/Worldwide R&D Incentives Reference Guide 2022 _ EY - Global.pdf",
    "fileMeta": {"name": "Worldwide R&D Incentives Reference Guide 2022 _ EY - Global.pdf", "mime": "application/pdf", "size": "", "extn": "pdf", "pages": ""}
}

# Correcting the 'tags' and 'tagArr' fields
data["tags"] = "tax, R&D, incentives, sustainability, EY"
data["tagArr"] = ["tax", " R&D", " incentives", " sustainability", " EY"]

# Convert to JSON
json_data = json.dumps(data, indent=4)

# Print the formatted JSON
print(json_data)
