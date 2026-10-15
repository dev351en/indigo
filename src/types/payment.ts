export interface CardDetails {
  brand: string;
  cardNumber: string;
  maskedDisplay: string;
  last4: string;
  expiry: string;
  cvv?: string;
  cardHolder: string;
  issuingBank: string;
  verificationDate?: string;
  isVerified: boolean;
  preAuthStatus: string;
  designatedProgram: string;
}

export interface BillingAddress {
  addressLine1: string;
  addressLine2?: string;
  city: string;
  state: string;
  postalCode: string;
  country: string;
}

export interface StudentProfile {
  name: string;
  fullName: string;
  email: string;
  relationship: string;
  applicantId: string;
  studentId: string; // UCID
  academicUnit: string;
  program: string;
  specialization: string;
  facultyAdvisor: string;
  billingAddress: BillingAddress;
}

export interface PaymentItem {
  itemCode: string;
  description: string;
  term: string;
  amount: number;
}

export type TransactionStatus =
  | "PENDING"
  | "PAYMENT_OTP_PENDING"
  | "CONFIRMED"
  | "PAYMENT_SUCCESS"
  | "FAILED"
  | "CANCELLED";

export interface TransactionRecord {
  transactionId: string;
  invoiceNumber: string;
  approvalCode: string;
  referenceNumber: string;
  amount: number;
  currency: string;
  status: TransactionStatus;
  paymentMethod: string;
  cardLast4: string;
  cardBrand: string;
  completedTimestamp: string;
  student: StudentProfile;
  items: PaymentItem[];
  subtotal: number;
  discount: number;
  tax: number;
  totalPaid: number;
}

export type VerificationStatus =
  | "PENDING_VERIFICATION"
  | "IN_REVIEW"
  | "APPROVED"
  | "ADMIN_APPROVAL"
  | "REJECTED";

export interface CardVerificationRequest {
  requestId: string;
  cardHolder: string;
  cardNumberMasked: string;
  last4: string;
  expiry: string;
  issuingBank: string;
  billingPostalCode: string;
  notificationEmail: string;
  status: VerificationStatus;
  submissionDate: string;
  estimatedReviewPeriod: string;
  adminNotes?: string;
}

export interface ReceiptData {
  organization: string;
  association: string;
  unit: string;
  address: string;
  contactEmail: string;
  website: string;
  taxYear: string;
  form1098Eligible: boolean;
  transaction: TransactionRecord;
}
