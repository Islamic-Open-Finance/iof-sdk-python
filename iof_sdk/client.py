"""Main IOF SDK Client."""

from typing import Any

from .base_client import BaseClient

# Agent Rail
from .rails.agent_rail import AgentRailClient

# Core Rails
from .rails.access_consent import AccessConsentRail
from .rails.account_information import AccountInformationRail
from .rails.aml import AmlRail
from .rails.analytics import AnalyticsRail
from .rails.cases import CasesRail
from .rails.clearing import ClearingRail
from .rails.compliance import ComplianceRail
from .rails.consent import ConsentRail
from .rails.contract_lifecycle import ContractLifecycleRail
from .rails.contracts import ContractsRail
from .rails.developer import DeveloperRail
from .rails.disputes import DisputesRail
from .rails.events import EventsRail
from .rails.governance import GovernanceRail
from .rails.jurisdictions import JurisdictionsRail
from .rails.kyc import KycRail
from .rails.legal import LegalRail
from .rails.messages import MessagesRail
from .rails.notifications import NotificationsRail
from .rails.observability import ObservabilityRail
from .rails.partners import PartnersRail
from .rails.portfolio import PortfolioRail
from .rails.reconciliation import ReconciliationRail
from .rails.reporting import ReportingRail
from .rails.risk import RiskRail
from .rails.routing import RoutingRail
from .rails.search import SearchRail
from .rails.treasury import TreasuryRail
from .rails.underwriting import UnderwritingRail
from .rails.webhooks import WebhooksRail
from .rails.zakat import ZakatRail

# Islamic Contract Rails
from .rails.diminishing_musharakah import DiminishingMusharakahRail
from .rails.hawalah import HawalahRail
from .rails.hibah import HibahRail
from .rails.ibraa import IbraaRail
from .rails.ijarah import IjarahRail
from .rails.istisna import IstisnaRail
from .rails.jualah import JualahRail
from .rails.kafalah import KafalahRail
from .rails.mudarabah import MudarabahRail
from .rails.muqasah import MuqasahRail
from .rails.murabaha import MurabahaRail
from .rails.musharakah import MusharakahRail
from .rails.qard import QardRail
from .rails.rahnu import RahnuRail
from .rails.salam import SalamRail
from .rails.tabarru import TabarruRail
from .rails.ujrah import UjrahRail
from .rails.wadiah import WadiahRail
from .rails.wakalah import WakalahRail

# Specialized Domain Rails
from .rails.debt import DebtRail
from .rails.funds import FundsRail
from .rails.fx import FxRail
from .rails.omnichannel import OmnichannelRail
from .rails.prudential import PrudentialRail
from .rails.shariah import ShariahComplianceRail, ShariahGovernanceRail, ShariahRulesRail
from .rails.sukuk import SukukRail
from .rails.takaful import TakafulRail
from .rails.trade_finance import TradeFinanceRail
from .rails.waqf import QardHasanRail, SadaqahRail, WaqfRail

# Platform Service Rails
from .rails.platform import (
    AuditRail,
    BillingRail,
    DashboardRail,
    LiquidityRail,
    MetadataRail,
    PaymentsRail,
    ProfitDistributionRail,
    ReferenceDataRail,
    WorkspacesRail,
)

# Additional Rails
from .rails.alerting import AlertingRail
from .rails.api_keys import ApiKeysRail
from .rails.asset_finance import AssetFinanceRail
from .rails.audit_analytics import AuditAnalyticsRail
from .rails.byoc import BYOCRail
from .rails.evidence_pack import EvidencePackRail
from .rails.finops import FinOpsRail
from .rails.gdpr import GDPRRail
from .rails.invitations import InvitationsRail
from .rails.islamic_microfinance import IslamicMicrofinanceRail
from .rails.notification_hub import NotificationHubRail
from .rails.passkeys import PasskeysRail
from .rails.products import ProductsRail
from .rails.programs import ProgramsRail
from .rails.residency import ResidencyRail
from .rails.retention import RetentionRail
from .rails.secrets import SecretsRail
from .rails.shariah_screening import ShariahScreeningRail
from .rails.taxonomy import TaxonomyRail


class IOFClient:
    """Islamic Open Finance Platform Client.

    Provides access to all 142 IOF API rails through a single client instance.
    One shared HTTP client is used for all rails.

    Args:
        api_key: Your API key
        base_url: API base URL (default: https://api.islamicopenfinance.com)
        timeout: Request timeout in seconds (default: 30)

    Example:
        client = IOFClient(api_key='your-api-key')
        accounts = client.accounts.list_accounts()
        contracts = client.contracts.list_contracts()
        murabaha = client.murabaha.list_contracts()
        sukuk = client.sukuk.list_issuances()
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.islamicopenfinance.com",
        timeout: int = 30,
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout

        # Shared HTTP client for all rails
        self._http = BaseClient(api_key, base_url, timeout)

        # =====================================================================
        # Agent Rail (Deterministic Agents)
        # =====================================================================
        self.agents = AgentRailClient(self._http)

        # =====================================================================
        # Account & Core Services
        # =====================================================================
        self.accounts = AccountInformationRail(self._http)
        self.contracts = ContractsRail(self._http)
        self.contract_lifecycle = ContractLifecycleRail(self._http)
        self.workspaces = WorkspacesRail(self._http)
        self.zakat = ZakatRail(self._http)

        # =====================================================================
        # Islamic Contract Types (19 Shariah-compliant contract rails)
        # =====================================================================
        self.murabaha = MurabahaRail(self._http)
        self.ijarah = IjarahRail(self._http)
        self.musharakah = MusharakahRail(self._http)
        self.diminishing_musharakah = DiminishingMusharakahRail(self._http)
        self.mudarabah = MudarabahRail(self._http)
        self.salam = SalamRail(self._http)
        self.istisna = IstisnaRail(self._http)
        self.wakalah = WakalahRail(self._http)
        self.wadiah = WadiahRail(self._http)
        self.qard = QardRail(self._http)
        self.kafalah = KafalahRail(self._http)
        self.rahnu = RahnuRail(self._http)
        self.hawalah = HawalahRail(self._http)
        self.tabarru = TabarruRail(self._http)
        self.hibah = HibahRail(self._http)
        self.ujrah = UjrahRail(self._http)
        self.jualah = JualahRail(self._http)
        self.ibraa = IbraaRail(self._http)
        self.muqasah = MuqasahRail(self._http)

        # =====================================================================
        # Shariah Governance
        # =====================================================================
        self.shariah_governance = ShariahGovernanceRail(self._http)
        self.shariah_rules = ShariahRulesRail(self._http)
        self.shariah_compliance = ShariahComplianceRail(self._http)

        # =====================================================================
        # Capital Markets & Sukuk
        # =====================================================================
        self.sukuk = SukukRail(self._http)

        # =====================================================================
        # Islamic Funds
        # =====================================================================
        self.funds = FundsRail(self._http)

        # =====================================================================
        # Takaful (Islamic Insurance)
        # =====================================================================
        self.takaful = TakafulRail(self._http)

        # =====================================================================
        # Waqf & Social Finance
        # =====================================================================
        self.waqf = WaqfRail(self._http)
        self.sadaqah = SadaqahRail(self._http)
        self.qard_hasan = QardHasanRail(self._http)

        # =====================================================================
        # Trade Finance
        # =====================================================================
        self.trade_finance = TradeFinanceRail(self._http)

        # =====================================================================
        # Debt & Receivables
        # =====================================================================
        self.debt = DebtRail(self._http)

        # =====================================================================
        # Foreign Exchange
        # =====================================================================
        self.fx = FxRail(self._http)

        # =====================================================================
        # Compliance & Risk
        # =====================================================================
        self.compliance = ComplianceRail(self._http)
        self.kyc = KycRail(self._http)
        self.aml = AmlRail(self._http)
        self.risk = RiskRail(self._http)

        # =====================================================================
        # Prudential & Basel III
        # =====================================================================
        self.prudential = PrudentialRail(self._http)

        # =====================================================================
        # Operations
        # =====================================================================
        self.clearing = ClearingRail(self._http)
        self.reconciliation = ReconciliationRail(self._http)
        self.cases = CasesRail(self._http)
        self.disputes = DisputesRail(self._http)
        self.routing = RoutingRail(self._http)
        self.payments = PaymentsRail(self._http)

        # =====================================================================
        # Financial Services
        # =====================================================================
        self.treasury = TreasuryRail(self._http)
        self.portfolio = PortfolioRail(self._http)
        self.underwriting = UnderwritingRail(self._http)
        self.liquidity = LiquidityRail(self._http)
        self.profit_distribution = ProfitDistributionRail(self._http)

        # =====================================================================
        # Platform Services
        # =====================================================================
        self.analytics = AnalyticsRail(self._http)
        self.reporting = ReportingRail(self._http)
        self.search = SearchRail(self._http)
        self.observability = ObservabilityRail(self._http)
        self.dashboard = DashboardRail(self._http)
        self.billing = BillingRail(self._http)
        self.audit = AuditRail(self._http)
        self.metadata = MetadataRail(self._http)
        self.reference_data = ReferenceDataRail(self._http)

        # =====================================================================
        # Governance & Legal
        # =====================================================================
        self.governance = GovernanceRail(self._http)
        self.legal = LegalRail(self._http)
        self.jurisdictions = JurisdictionsRail(self._http)

        # =====================================================================
        # Developer & Integration
        # =====================================================================
        self.developer = DeveloperRail(self._http)
        self.webhooks = WebhooksRail(self._http)
        self.events = EventsRail(self._http)
        self.notifications = NotificationsRail(self._http)
        self.messages = MessagesRail(self._http)

        # =====================================================================
        # Access & Consent
        # =====================================================================
        self.access_consent = AccessConsentRail(self._http)
        self.consent = ConsentRail(self._http)

        # =====================================================================
        # Partner Management
        # =====================================================================
        self.partners = PartnersRail(self._http)

        # =====================================================================
        # Omnichannel
        # =====================================================================
        self.omnichannel = OmnichannelRail(self._http)

        # =====================================================================
        # Additional Rails
        # =====================================================================
        self.alerting = AlertingRail(self._http)
        self.api_keys = ApiKeysRail(self._http)
        self.asset_finance = AssetFinanceRail(self._http)
        self.audit_analytics = AuditAnalyticsRail(self._http)
        self.byoc = BYOCRail(self._http)
        self.evidence_pack = EvidencePackRail(self._http)
        self.finops = FinOpsRail(self._http)
        self.gdpr = GDPRRail(self._http)
        self.invitations = InvitationsRail(self._http)
        self.islamic_microfinance = IslamicMicrofinanceRail(self._http)
        self.notification_hub = NotificationHubRail(self._http)
        self.passkeys = PasskeysRail(self._http)
        self.products = ProductsRail(self._http)
        self.programs = ProgramsRail(self._http)
        self.residency = ResidencyRail(self._http)
        self.retention = RetentionRail(self._http)
        self.secrets = SecretsRail(self._http)
        self.shariah_screening = ShariahScreeningRail(self._http)
        self.taxonomy = TaxonomyRail(self._http)

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._http.close()

    def __enter__(self) -> "IOFClient":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def __repr__(self) -> str:
        return f"IOFClient(base_url={self.base_url})"
