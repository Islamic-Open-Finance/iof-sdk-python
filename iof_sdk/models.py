"""
Type definitions for the IOF SDK.

This module provides TypedDict definitions for request and response models
used throughout the Islamic Open Finance API.
"""

from typing import Any, Dict, List, Literal, Optional, TypedDict, Union
from typing_extensions import NotRequired


# ============================================================================
# Common Types
# ============================================================================


class PaginationInfo(TypedDict):
    """Pagination metadata."""

    page: int
    limit: int
    total: int
    pages: int


class PaginatedResponse(TypedDict):
    """Generic paginated response."""

    data: List[Dict[str, Any]]
    pagination: PaginationInfo


# ============================================================================
# Contract Types
# ============================================================================


class Contract(TypedDict):
    """Islamic finance contract."""

    id: str
    type: str
    status: str
    principal: float
    currency: str
    created_at: str
    updated_at: str
    parties: NotRequired[List[Dict[str, Any]]]
    terms: NotRequired[Dict[str, Any]]


class CreateContractRequest(TypedDict):
    """Request to create a new contract."""

    type: str
    principal: float
    currency: str
    parties: List[Dict[str, Any]]
    terms: NotRequired[Dict[str, Any]]


class UpdateContractRequest(TypedDict, total=False):
    """Request to update a contract."""

    status: str
    terms: Dict[str, Any]


class ValidationResult(TypedDict):
    """Contract validation result."""

    valid: bool
    errors: NotRequired[List[str]]
    warnings: NotRequired[List[str]]


# ============================================================================
# Jurisdiction Types
# ============================================================================


class Jurisdiction(TypedDict):
    """Jurisdiction configuration."""

    id: str
    name: str
    code: str
    country: str
    regulatory_authority: str
    shariah_board: NotRequired[str]
    created_at: str
    updated_at: str


# ============================================================================
# Consent Types
# ============================================================================


class Consent(TypedDict):
    """Access consent."""

    id: str
    status: str
    type: str
    permissions: List[str]
    expires_at: str
    created_at: str
    updated_at: str


class CreateConsentRequest(TypedDict):
    """Request to create a consent."""

    type: str
    permissions: List[str]
    expires_at: NotRequired[str]


# ============================================================================
# KYC Types
# ============================================================================


class Customer(TypedDict):
    """Customer information."""

    id: str
    type: str
    status: str
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    phone: NotRequired[str]
    created_at: str
    updated_at: str


class CreateCustomerRequest(TypedDict):
    """Request to create a customer."""

    type: Literal["individual", "corporate"]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    phone: NotRequired[str]


class ScreeningResult(TypedDict):
    """Screening result."""

    customer_id: str
    status: str
    matched: bool
    matches: NotRequired[List[Dict[str, Any]]]


# ============================================================================
# AML Types
# ============================================================================


class AmlRule(TypedDict):
    """AML rule configuration."""

    id: str
    name: str
    description: str
    severity: str
    enabled: bool
    conditions: Dict[str, Any]
    created_at: str
    updated_at: str


class AmlScreening(TypedDict):
    """AML screening record."""

    id: str
    entity_id: str
    entity_type: str
    status: str
    risk_score: float
    matches: List[Dict[str, Any]]
    created_at: str
    updated_at: str


class AmlAlert(TypedDict):
    """AML alert."""

    id: str
    type: str
    severity: str
    status: str
    entity_id: str
    description: str
    created_at: str
    updated_at: str


class AmlCase(TypedDict):
    """AML case."""

    id: str
    title: str
    status: str
    priority: str
    assigned_to: NotRequired[str]
    alerts: List[str]
    created_at: str
    updated_at: str


# ============================================================================
# Developer Types
# ============================================================================


class DeveloperClient(TypedDict):
    """OAuth/API client."""

    id: str
    name: str
    description: NotRequired[str]
    client_id: str
    client_secret: NotRequired[str]
    redirect_uris: List[str]
    created_at: str
    updated_at: str


class ApiKey(TypedDict):
    """API key."""

    id: str
    name: str
    key: NotRequired[str]
    prefix: str
    scopes: List[str]
    expires_at: NotRequired[str]
    last_used_at: NotRequired[str]
    created_at: str
    updated_at: str


# ============================================================================
# Partner Types
# ============================================================================


class Partner(TypedDict):
    """Partner account."""

    id: str
    name: str
    type: str
    status: str
    revenue_share_percentage: NotRequired[float]
    created_at: str
    updated_at: str


class Program(TypedDict):
    """Partner program."""

    id: str
    name: str
    type: str
    commission_rate: float
    status: str
    created_at: str
    updated_at: str


# ============================================================================
# Dispute Types
# ============================================================================


class Dispute(TypedDict):
    """Dispute record."""

    id: str
    type: str
    status: str
    amount: float
    currency: str
    reason: str
    created_at: str
    updated_at: str


# ============================================================================
# Zakat Types
# ============================================================================


class ZakatCalculation(TypedDict):
    """Zakat calculation."""

    id: str
    account_id: str
    year: int
    total_wealth: float
    nisab: float
    zakat_due: float
    currency: str
    status: str
    created_at: str
    updated_at: str


class ZakatPayment(TypedDict):
    """Zakat payment."""

    id: str
    calculation_id: str
    amount: float
    currency: str
    status: str
    paid_at: NotRequired[str]
    created_at: str
    updated_at: str


# ============================================================================
# Reconciliation Types
# ============================================================================


class ReconciliationJob(TypedDict):
    """Reconciliation job."""

    id: str
    name: str
    status: str
    matched_count: int
    unmatched_count: int
    exception_count: int
    created_at: str
    updated_at: str


class ReconciliationException(TypedDict):
    """Reconciliation exception."""

    id: str
    job_id: str
    type: str
    status: str
    description: str
    amount_difference: NotRequired[float]
    created_at: str
    updated_at: str


# ============================================================================
# Observability Types
# ============================================================================


class SloMetric(TypedDict):
    """Service Level Objective metric."""

    id: str
    name: str
    target: float
    current: float
    status: str
    period: str
    created_at: str
    updated_at: str


class AuditLog(TypedDict):
    """Audit log entry."""

    id: str
    event_type: str
    actor_id: str
    resource_type: str
    resource_id: str
    action: str
    metadata: NotRequired[Dict[str, Any]]
    ip_address: NotRequired[str]
    user_agent: NotRequired[str]
    created_at: str


class ShariahMonitoringRecord(TypedDict):
    """Shariah monitoring record."""

    id: str
    contract_id: str
    check_type: str
    status: str
    result: str
    flags: NotRequired[List[str]]
    created_at: str
    updated_at: str


class DataExport(TypedDict):
    """Data export job."""

    id: str
    type: str
    status: str
    format: str
    url: NotRequired[str]
    expires_at: NotRequired[str]
    created_at: str
    updated_at: str


# ============================================================================
# Message Types
# ============================================================================


class Message(TypedDict):
    """ISO 20022 message."""

    id: str
    type: str
    direction: str
    status: str
    content: Dict[str, Any]
    created_at: str
    updated_at: str


# ============================================================================
# Event Types
# ============================================================================


class Event(TypedDict):
    """Event record."""

    id: str
    type: str
    source: str
    data: Dict[str, Any]
    created_at: str


class Webhook(TypedDict):
    """Webhook configuration."""

    id: str
    url: str
    events: List[str]
    secret: NotRequired[str]
    enabled: bool
    created_at: str
    updated_at: str


# ============================================================================
# Notification Types
# ============================================================================


class Notification(TypedDict):
    """Notification record."""

    id: str
    type: str
    channel: str
    recipient: str
    subject: NotRequired[str]
    body: str
    status: str
    sent_at: NotRequired[str]
    created_at: str
    updated_at: str


# ============================================================================
# Search Types
# ============================================================================


class SearchResult(TypedDict):
    """Search result."""

    hits: List[Dict[str, Any]]
    total: int
    query: str
    took: int


# ============================================================================
# Case Types
# ============================================================================


class Case(TypedDict):
    """Case record."""

    id: str
    type: str
    status: str
    priority: str
    title: str
    description: NotRequired[str]
    assigned_to: NotRequired[str]
    created_at: str
    updated_at: str


# ============================================================================
# Routing Types
# ============================================================================


class RoutingRule(TypedDict):
    """Routing rule."""

    id: str
    name: str
    priority: int
    conditions: Dict[str, Any]
    destination: str
    enabled: bool
    created_at: str
    updated_at: str


# ============================================================================
# Financial Rails Types
# ============================================================================


class ClearingBatch(TypedDict):
    """Clearing batch."""

    id: str
    status: str
    total_transactions: int
    total_amount: float
    currency: str
    created_at: str
    updated_at: str


class TreasuryPosition(TypedDict):
    """Treasury position."""

    id: str
    account_id: str
    currency: str
    balance: float
    available: float
    reserved: float
    updated_at: str


class RiskLimit(TypedDict):
    """Risk limit."""

    id: str
    name: str
    type: str
    limit_amount: float
    current_exposure: float
    currency: str
    status: str
    created_at: str
    updated_at: str


class Portfolio(TypedDict):
    """Investment portfolio."""

    id: str
    name: str
    type: str
    total_value: float
    currency: str
    created_at: str
    updated_at: str


class Report(TypedDict):
    """Generated report."""

    id: str
    name: str
    type: str
    format: str
    status: str
    url: NotRequired[str]
    created_at: str
    updated_at: str


# ============================================================================
# Governance Types
# ============================================================================


class LegalDocument(TypedDict):
    """Legal document."""

    id: str
    name: str
    type: str
    version: str
    status: str
    content: NotRequired[str]
    created_at: str
    updated_at: str


class UnderwritingDecision(TypedDict):
    """Underwriting decision."""

    id: str
    application_id: str
    decision: str
    risk_score: float
    conditions: NotRequired[List[str]]
    created_at: str
    updated_at: str


class ComplianceCheck(TypedDict):
    """Compliance check."""

    id: str
    type: str
    status: str
    result: str
    findings: NotRequired[List[str]]
    created_at: str
    updated_at: str


class GovernanceBoard(TypedDict):
    """Shariah/governance board."""

    id: str
    name: str
    type: str
    members: List[Dict[str, Any]]
    created_at: str
    updated_at: str
