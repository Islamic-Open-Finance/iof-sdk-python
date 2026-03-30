"""Basel III Rail API client."""

from typing import Any, List, Optional


class BaselRail:
    """
    Basel III Rail API client.

    Provides Basel III regulatory compliance capabilities:
    - Capital adequacy ratios (CET1, Tier 1, Total)
    - Liquidity coverage ratio (LCR) and net stable funding ratio (NSFR)
    - Leverage ratio monitoring
    - Stress testing
    - Regulatory reporting
    - Exposure and concentration risk
    """

    def __init__(self, http_client: Any) -> None:
        """Initialize the Basel III rail client."""
        self.http = http_client
        self.base_path = "/api/v1/basel"

    # Capital Adequacy

    def get_capital_ratios(self) -> dict:
        """
        Get capital ratios (CET1, Tier 1, Total Capital).

        Returns:
            Capital ratios and risk-weighted assets
        """
        return self.http.get(f"{self.base_path}/capital/ratios")

    def get_capital_adequacy(self) -> dict:
        """
        Get capital adequacy status.

        Returns:
            Capital adequacy details and compliance status
        """
        return self.http.get(f"{self.base_path}/capital/adequacy")

    def get_risk_weighted_assets(self) -> dict:
        """
        Get risk-weighted assets breakdown.

        Returns:
            Credit, market, and operational risk RWA
        """
        return self.http.get(f"{self.base_path}/capital/risk-weighted-assets")

    def get_capital_composition(self) -> dict:
        """
        Get capital composition (CET1, AT1, Tier 2).

        Returns:
            Capital composition details
        """
        return self.http.get(f"{self.base_path}/capital/composition")

    # Liquidity

    def get_lcr(self) -> dict:
        """
        Get Liquidity Coverage Ratio (LCR).

        Returns:
            LCR, HQLA, net cash outflows, and compliance status
        """
        return self.http.get(f"{self.base_path}/liquidity/lcr")

    def get_nsfr(self) -> dict:
        """
        Get Net Stable Funding Ratio (NSFR).

        Returns:
            NSFR, available/required stable funding, compliance status
        """
        return self.http.get(f"{self.base_path}/liquidity/nsfr")

    def get_hqla_composition(self) -> dict:
        """
        Get High Quality Liquid Assets composition.

        Returns:
            Level 1, 2A, 2B HQLA breakdown
        """
        return self.http.get(f"{self.base_path}/liquidity/hqla")

    def get_maturity_ladder(self) -> dict:
        """
        Get maturity ladder for liquidity analysis.

        Returns:
            Maturity buckets with inflows, outflows, and positions
        """
        return self.http.get(f"{self.base_path}/liquidity/maturity-ladder")

    # Leverage

    def get_leverage_ratio(self) -> dict:
        """
        Get leverage ratio.

        Returns:
            Leverage ratio, Tier 1 capital, total exposure
        """
        return self.http.get(f"{self.base_path}/leverage/ratio")

    # Stress Testing

    def list_stress_tests(self, status: Optional[str] = None) -> list:
        """
        List stress test results.

        Args:
            status: Filter by status

        Returns:
            List of stress test results
        """
        params = {"status": status}
        return self.http.get(f"{self.base_path}/stress-tests", params=params)

    def get_stress_test(self, test_id: str) -> dict:
        """
        Get stress test result by ID.

        Args:
            test_id: Stress test ID

        Returns:
            Stress test result details
        """
        return self.http.get(f"{self.base_path}/stress-tests/{test_id}")

    def execute_stress_test(self, scenarios: list) -> dict:
        """
        Execute a stress test with given scenarios.

        Args:
            scenarios: List of stress test scenarios

        Returns:
            Test execution confirmation with test ID
        """
        return self.http.post(
            f"{self.base_path}/stress-tests", json={"scenarios": scenarios}
        )

    # Regulatory Reporting

    def list_regulatory_reports(self, status: Optional[str] = None) -> list:
        """
        List regulatory reports.

        Args:
            status: Filter by status

        Returns:
            List of regulatory reports
        """
        params = {"status": status}
        return self.http.get(f"{self.base_path}/regulatory-reports", params=params)

    def generate_report(self, report_type: str, period_start: str, period_end: str) -> dict:
        """
        Generate a regulatory report.

        Args:
            report_type: Report type (REPORT_217, REPORT_220, etc.)
            period_start: Period start date (ISO format)
            period_end: Period end date (ISO format)

        Returns:
            Generated regulatory report
        """
        data = {
            "reportType": report_type,
            "periodStart": period_start,
            "periodEnd": period_end,
        }
        return self.http.post(f"{self.base_path}/regulatory-reports", json=data)

    def get_report(self, report_id: str) -> dict:
        """
        Get regulatory report by ID.

        Args:
            report_id: Report ID

        Returns:
            Regulatory report details
        """
        return self.http.get(f"{self.base_path}/regulatory-reports/{report_id}")

    # Exposure

    def get_counterparty_exposures(self, limit: Optional[int] = None) -> list:
        """
        Get counterparty exposure data.

        Args:
            limit: Maximum number of results

        Returns:
            List of counterparty exposures
        """
        params = {"limit": limit}
        return self.http.get(f"{self.base_path}/exposures/counterparty", params=params)

    def get_concentration_risk(self, dimension: Optional[str] = None) -> list:
        """
        Get concentration risk analysis.

        Args:
            dimension: Dimension (sector, geography, counterparty, product)

        Returns:
            List of concentration risk entries
        """
        params = {"dimension": dimension}
        return self.http.get(f"{self.base_path}/exposures/concentration", params=params)

    def get_large_exposures(self) -> list:
        """
        Get large exposures.

        Returns:
            List of large exposure entries
        """
        return self.http.get(f"{self.base_path}/exposures/large")

    # Compliance

    def get_compliance_assertions(self) -> list:
        """
        Get compliance assertions.

        Returns:
            List of compliance assertions
        """
        return self.http.get(f"{self.base_path}/compliance/assertions")

    def run_compliance_validation(self) -> dict:
        """
        Run compliance validation.

        Returns:
            Validation result with pass/fail and assertions
        """
        return self.http.post(f"{self.base_path}/compliance/validate")

    # Evidence

    def generate_evidence_pack(self, scope: str, period_start: str, period_end: str) -> dict:
        """
        Generate an evidence pack for auditors.

        Args:
            scope: Evidence scope
            period_start: Period start date
            period_end: Period end date

        Returns:
            Generated evidence pack with artifacts
        """
        data = {"scope": scope, "periodStart": period_start, "periodEnd": period_end}
        return self.http.post(f"{self.base_path}/evidence-pack", json=data)
