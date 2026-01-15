



✅ Data Engineering Scenario-Based Questions

1) A pipeline failed at 2 AM. What steps do you take?
Answer:First, check logs and alerts. Identify where it broke (e.g., data source, transformation, destination), fix the issue, rerun if needed, and document root cause.

2) A CSV file has inconsistent columns every day. How do you handle it?
Answer:I’d build a dynamic parser in Python or use schema inference to handle variations, log errors, and flag rows for review.

3) Data from an API is missing on some days. What’s your strategy?
Answer:I’d implement retries with exponential backoff, add data validation checks, and alert systems to notify failures in extraction.

4) Your Spark job is taking too long. What do you do?
Answer:Optimize partitioning, avoid wide transformations, cache intermediate results, and scale cluster resources if needed.

5) Stakeholders want near real-time data instead of daily reports. How do you upgrade the pipeline?
Answer:I’d evaluate streaming tools like Kafka, Flink, or Spark Streaming and re-architect the pipeline for incremental ingestion and processing.

6) You’re asked to migrate an ETL pipeline to the cloud. What’s your approach?
Answer:Analyze current stack, choose equivalent cloud tools (e.g., AWS Glue, GCP Dataflow), refactor for scalability, test, then migrate with rollback plan.

7) Data volume suddenly spikes. What do you investigate?
Answer:Check for source changes, duplication, or batch issues. Validate schema, deduplicate, and review pipeline thresholds.

8) A team complains about schema changes breaking their reports. How do you manage schema evolution?
Answer: Implement versioning, use schema registry (if available), enforce contracts, and set up notifications for breaking changes.

9) Your data lake is becoming messy. What’s your strategy?
Answer:Apply governance: use folder structures, naming conventions, metadata tagging, lifecycle policies, and automate cleanup.

10) You need to backfill 2 years of data without impacting current workflows. What do you do?
Answer:Run backfill as a separate batch process in isolated storage, throttle resources to avoid contention, and merge carefully with validation.
