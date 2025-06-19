# 📦 Data Decoded: Amazon's Customer-Product Interaction

A data engineering and analytics project designed to improve Amazon's automotive shopping experience by integrating **MongoDB**, **Neo4j**, and **Flask**. This system helps customers explore product details more effectively and enables Amazon to uncover actionable insights from product interaction data.

## Team
**Group 9**  
Geer Hong · Pulkit Diwan · Theophilus Poku Brefo · Wenyang Cao · Danyu Li

---

## Project Goal
To develop a **search and recommendation engine** for Amazon’s automotive category using:
- Large-scale customer reviews and product metadata (3.6 GB total)
- Graph databases to reveal store-category relationships
- NoSQL document databases for flexible querying
- Flask web app to expose the insights to users interactively

---

## Data Sources
- **Amazon Customer Reviews** (2.32 GB)
- **Amazon Product Metadata** (1.28 GB)  
Source: [McAuley Lab Amazon Reviews 2023](https://amazon-reviews-2023.github.io/main.html)

Each dataset includes:
- Reviews, ratings, product IDs, reviewer IDs, timestamps
- Product title, average rating, category hierarchy, price, store, description

---

## Technologies & Tools

| Tool       | Purpose                                             |
|------------|-----------------------------------------------------|
| **MongoDB**| Stores and queries JSON-based product data         |
| **Neo4j**  | Analyzes and visualizes relationships between stores and categories |
| **Flask**  | Web interface for search and visualization         |
| **AWS EC2**| Hosts MongoDB, Neo4j, and Flask servers            |

---

## Business Applications
- 📌 Identify top-performing product categories to **increase sales**
- 🧠 Leverage search and sales data to **spot trends**
- 💰 Evaluate price elasticity to **optimize pricing**
- 🎯 Tailor marketing and inventory to **purchasing patterns**

---

## Visualization & Insights
- Neo4j used to cluster and map products into categories like **Truck Bed Accessories**
- Identified central stores (e.g., **Tyger Auto**, **Uxcell**) based on connection density
- Ratings and product connections helped prioritize partnerships and strategies

---

## Data Governance
- **Security:** Encrypted data, MFA, access controls
- **Integrity:** Validation & monitoring for tampering
- **Compliance:** Meets GDPR, CCPA for customer data

---

## Estimated Cost Breakdown
| Component         | Monthly Cost |
|------------------|--------------|
| Neo4j on EC2      | $404.42      |
| Flask + API EC2   | $500.00      |
| DocumentDB (Mongo)| $539.47      |
| **Total**         | **$1,443**   |

---

## Future Recommendations
- Integrate **Kafka** for real-time data streams
- Expand product categories beyond automotive
- Implement **ML models** for recommendations
- Benchmark performance under high load
- Explore cloud cost optimization

---

## License & Acknowledgments
Data provided by [McAuley Lab](https://amazon-reviews-2023.github.io/main.html). Public and freely accessible. Please cite the dataset appropriately.

---

## Contact
**Wenyang Cao**  
[Email](mailto:wenyangcao99@gmail.com) · [LinkedIn](https://linkedin.com/in/wenyangcao)  
