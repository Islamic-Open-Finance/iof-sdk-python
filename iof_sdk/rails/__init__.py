"""Islamic Open Finance Rails - All 142 rail clients."""

# Core Rails
from .agent_rail import AgentRailClient
from .access_consent import AccessConsentRail
from .account_information import Account, AccountInformationRail, Statement, Transaction
from .aml import AmlRail
from .analytics import AnalyticsRail
from .cases import CasesRail
from .clearing import ClearingRail
from .compliance import ComplianceRail
from .consent import ConsentRail
from .contract_lifecycle import ContractLifecycleRail
from .contracts import ContractsRail
from .developer import DeveloperRail
from .disputes import DisputesRail
from .events import EventsRail
from .governance import GovernanceRail
from .jurisdictions import JurisdictionsRail
from .kyc import KycRail
from .legal import LegalRail
from .messages import MessagesRail
from .notifications import NotificationsRail
from .observability import ObservabilityRail
from .partners import PartnersRail
from .portfolio import PortfolioRail
from .reconciliation import ReconciliationRail
from .reporting import ReportingRail
from .risk import RiskRail
from .routing import RoutingRail
from .search import SearchRail
from .treasury import TreasuryRail
from .underwriting import UnderwritingRail
from .webhooks import WebhooksRail
from .zakat import ZakatRail

# Islamic Contract Rails
from .diminishing_musharakah import DiminishingMusharakahRail
from .hawalah import HawalahRail
from .hibah import HibahRail
from .ibraa import IbraaRail
from .ijarah import IjarahRail
from .istisna import IstisnaRail
from .jualah import JualahRail
from .kafalah import KafalahRail
from .mudarabah import MudarabahRail
from .muqasah import MuqasahRail
from .murabaha import MurabahaRail
from .musharakah import MusharakahRail
from .qard import QardRail
from .rahnu import RahnuRail
from .salam import SalamRail
from .tabarru import TabarruRail
from .ujrah import UjrahRail
from .wadiah import WadiahRail
from .wakalah import WakalahRail

# Specialized Domain Rails
from .debt import DebtRail
from .funds import FundsRail
from .fx import FxRail
from .omnichannel import OmnichannelRail
from .prudential import PrudentialRail
from .shariah import ShariahComplianceRail, ShariahGovernanceRail, ShariahRulesRail
from .sukuk import SukukRail
from .takaful import TakafulRail
from .trade_finance import TradeFinanceRail
from .waqf import QardHasanRail, SadaqahRail, WaqfRail

# Platform Service Rails
from .platform import (
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
from .alerting import AlertingRail
from .api_keys import ApiKeysRail
from .asset_finance import AssetFinanceRail
from .audit_analytics import AuditAnalyticsRail
from .byoc import BYOCRail
from .evidence_pack import EvidencePackRail
from .finops import FinOpsRail
from .gdpr import GDPRRail
from .invitations import InvitationsRail
from .islamic_microfinance import IslamicMicrofinanceRail
from .notification_hub import NotificationHubRail
from .passkeys import PasskeysRail
from .products import ProductsRail
from .programs import ProgramsRail
from .residency import ResidencyRail
from .retention import RetentionRail
from .secrets import SecretsRail
from .shariah_screening import ShariahScreeningRail
from .taxonomy import TaxonomyRail

# Backward compatibility
AccountInformationClient = AccountInformationRail

__all__ = [
    # Core
    "AccessConsentRail",
    "Account",
    "AccountInformationClient",
    "AccountInformationRail",
    "AmlRail",
    "AnalyticsRail",
    "AuditRail",
    "BillingRail",
    "CasesRail",
    "ClearingRail",
    "ComplianceRail",
    "ConsentRail",
    "ContractLifecycleRail",
    "ContractsRail",
    "DashboardRail",
    "DebtRail",
    "DeveloperRail",
    "DisputesRail",
    "EventsRail",
    "FundsRail",
    "FxRail",
    "GovernanceRail",
    "JurisdictionsRail",
    "KycRail",
    "LegalRail",
    "LiquidityRail",
    "MessagesRail",
    "MetadataRail",
    "NotificationsRail",
    "ObservabilityRail",
    "OmnichannelRail",
    "PartnersRail",
    "PaymentsRail",
    "PortfolioRail",
    "ProfitDistributionRail",
    "PrudentialRail",
    "ReconciliationRail",
    "ReferenceDataRail",
    "ReportingRail",
    "RiskRail",
    "RoutingRail",
    "SearchRail",
    "Statement",
    "Transaction",
    "TreasuryRail",
    "UnderwritingRail",
    "WebhooksRail",
    "WorkspacesRail",
    "ZakatRail",
    # Islamic Contracts
    "DiminishingMusharakahRail",
    "HawalahRail",
    "HibahRail",
    "IbraaRail",
    "IjarahRail",
    "IstisnaRail",
    "JualahRail",
    "KafalahRail",
    "MudarabahRail",
    "MuqasahRail",
    "MurabahaRail",
    "MusharakahRail",
    "QardRail",
    "RahnuRail",
    "SalamRail",
    "TabarruRail",
    "UjrahRail",
    "WadiahRail",
    "WakalahRail",
    # Specialized
    "QardHasanRail",
    "SadaqahRail",
    "ShariahComplianceRail",
    "ShariahGovernanceRail",
    "ShariahRulesRail",
    "SukukRail",
    "TakafulRail",
    "TradeFinanceRail",
    "WaqfRail",
    # Additional Rails
    "AlertingRail",
    "ApiKeysRail",
    "AssetFinanceRail",
    "AuditAnalyticsRail",
    "BYOCRail",
    "EvidencePackRail",
    "FinOpsRail",
    "GDPRRail",
    "InvitationsRail",
    "IslamicMicrofinanceRail",
    "NotificationHubRail",
    "PasskeysRail",
    "ProductsRail",
    "ProgramsRail",
    "ResidencyRail",
    "RetentionRail",
    "SecretsRail",
    "ShariahScreeningRail",
    "TaxonomyRail",
]
