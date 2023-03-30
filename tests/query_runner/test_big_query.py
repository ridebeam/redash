from unittest import TestCase


class TestBigQueryRunner(TestCase):
    annotated_query = """
        /* Task ID: 8ccd40c878f59fa69ccf31a72140b208, Query Hash: f6bf37efedbc0a2dfffc1caf5088d86e, Query ID: 12345, Queue: celery, Username: jezdez */
        SELECT * FROM users;
    """

    def test_big_query_query_runner_get_job_data(self, *args, **kwargs):
        query_runner = BigQuery({})
        job_data = query_runner._get_job_data(self.annotated_query)
        assert job_data["labels"] == {
            "redash_query_id": "12345",
        }
