import { Router, Request, Response } from "express";
import fs from "fs";
import path from "path";
import {
  CardDetails,
  TransactionRecord,
  CardVerificationRequest,
  ReceiptData,
  StudentProfile,
} from "../src/types/payment";

export const paymentRouter = Router();

// ============================================================================
// In-Memory Database & Seed Data Store
// ============================================================================

export const defaultStudent: StudentProfile = {
  name: "Devendra Dubey",
  fullName: "Devendra Dubey Biswambharnath Geeta",
  email: "devendra.dubey@iitgn.ac.in",
  relationship: "Self - Verified Remote Alumni / Admitted Doctoral Candidate",
  applicantId: "UC-2027-89321",
  studentId: "12489321",
  academicUnit: "Division of the Physical Sciences • Dept. of Chemistry",
  program: "Doctor of Philosophy (Ph.D.) in Chemistry",
  specialization: "Computational Chemistry & Catalysis",
  facultyAdvisor: "Prof. Alex (Alexander Q.) Cusumano",
  billingAddress: {
    addressLine1: "G-704, Lodha Elite",
    addressLine2: "Lodha Heaven",
    city: "Nilje",
    state: "Maharashtra",
    postalCode: "421204",
    country: "India",
  },
};

export const verifiedCardsMap: Record<string, CardDetails> = {
  "0405": {
    brand: "Discover Debit Card",
    cardNumber: "6522944548050405",
    maskedDisplay: "•••• •••• •••• 0405",
    last4: "0405",
    expiry: "04/32",
    cvv: "842",
    cardHolder: "Devendra Dubey",
    issuingBank: "Stanford Federal Credit Union / Global Partner Bank",
    verificationDate: "16th October 2026, 03:00:00 AM IST",
    isVerified: true,
    preAuthStatus: "Verified & Pre-Authorized Mandate Active",
    designatedProgram: "Ph.D. Chemistry (Autumn 2027)",
  },
  "4242": {
    brand: "Visa Debit Card",
    cardNumber: "4242424242424242",
    maskedDisplay: "•••• •••• •••• 4242",
    last4: "4242",
    expiry: "12/28",
    cvv: "123",
    cardHolder: "Devendra Dubey",
    issuingBank: "University Financial Services",
    verificationDate: "1st October 2026",
    isVerified: true,
    preAuthStatus: "Institutional Direct Debit Mandate",
    designatedProgram: "Ph.D. Chemistry (Autumn 2027)",
  },
};

export const transactionsStore: TransactionRecord[] = [
  {
    transactionId: "TXN-UCHI-APP-2026-100101",
    invoiceNumber: "INV-UCHI-APP-2026-100101",
    approvalCode: "AUTH-UCHI-APP-100101",
    referenceNumber: "REF-UCHI-APP-2026-90",
    amount: 90.0,
    currency: "USD",
    status: "CONFIRMED",
    paymentMethod: "Discover Debit Card (•••• 0405)",
    cardLast4: "0405",
    cardBrand: "Discover Debit Card",
    completedTimestamp: "2026-10-01T06:30:00+05:30",
    student: defaultStudent,
    items: [
      {
        itemCode: "UC-GRAD-APP-2027",
        description: "Graduate Application and Dossier Processing Fee — Doctor of Philosophy (Ph.D.) in Chemistry",
        term: "Autumn 2027",
        amount: 90.0,
      },
    ],
    subtotal: 90.0,
    discount: 0.0,
    tax: 0.0,
    totalPaid: 90.0,
  },
  {
    transactionId: "TXN-UCHI-2026-89321",
    invoiceNumber: "INV-UCHI-2026-89321",
    approvalCode: "AUTH-UCHI-89321",
    referenceNumber: "REF-UCHI-DEP-2027-6200",
    amount: 6200.0,
    currency: "USD",
    status: "CONFIRMED",
    paymentMethod: "Discover Debit Card (•••• 0405)",
    cardLast4: "0405",
    cardBrand: "Discover Debit Card",
    completedTimestamp: "2026-10-16T03:00:00+05:30",
    student: defaultStudent,
    items: [
      {
        itemCode: "UC-CHEM-PHD-2027",
        description: "Ph.D. Matriculation Seat Locking & Enrollment Deposit — Cusumano Research Group",
        term: "Autumn 2027",
        amount: 6200.0,
      },
    ],
    subtotal: 6200.0,
    discount: 0.0,
    tax: 0.0,
    totalPaid: 6200.0,
  },
];

export const verificationRequestsStore: CardVerificationRequest[] = [];

// OTP In-Memory Store
const otpStore: Record<string, { code: string; expiresAt: number; attempts: number }> = {};

// ============================================================================
// Router Endpoints
// ============================================================================

/**
 * 1. GET /api/payment/demo-card-info
 * Returns safe demo card placeholder data
 */
paymentRouter.get("/demo-card-info", (_req: Request, res: Response) => {
  const card = verifiedCardsMap["0405"];
  res.json({
    brand: card.brand,
    maskedDisplay: card.maskedDisplay,
    last4: card.last4,
    expiry: card.expiry,
    cardHolder: card.cardHolder,
    issuingBank: card.issuingBank,
    preAuthStatus: card.preAuthStatus,
    designatedProgram: card.designatedProgram,
  });
});

/**
 * 2. POST /api/payment/validate-card
 * Evaluates card number against verifiedCardsMap
 */
paymentRouter.post("/validate-card", (req: Request, res: Response) => {
  const { cardNumber } = req.body || {};
  const normalized = (cardNumber || "").replace(/\D/g, "");

  if (!normalized) {
    return res.status(400).json({ error: "Card number is required" });
  }

  const last4 = normalized.slice(-4);
  const matched = verifiedCardsMap[last4] || (normalized === "6522944548050405" ? verifiedCardsMap["0405"] : null);

  if (matched) {
    return res.json({
      status: "VERIFIED_DEMO_CARD",
      isVerified: true,
      message: "Pre-authorized verified card recognized.",
      card: {
        brand: matched.brand,
        maskedDisplay: matched.maskedDisplay,
        last4: matched.last4,
        expiry: matched.expiry,
        preAuthStatus: matched.preAuthStatus,
      },
    });
  }

  return res.json({
    status: "UNVERIFIED",
    isVerified: false,
    message: "Card not verified. It will take 15 to 20 days of verification.",
    canVerify: true,
    verificationUrl: "/verify-payment-method",
  });
});

/**
 * 3. POST /api/payment/create
 * Initiates payment. Rejects unverified cards.
 */
paymentRouter.post("/create", (req: Request, res: Response) => {
  const { cardNumber, amount } = req.body || {};
  const normalized = (cardNumber || "").replace(/\D/g, "");
  const last4 = normalized.slice(-4);
  const matched = verifiedCardsMap[last4] || (normalized === "6522944548050405" ? verifiedCardsMap["0405"] : null);

  if (!matched) {
    return res.status(400).json({
      error: "UNVERIFIED_CARD",
      message: "Card not verified. It will take 15 to 20 days of verification.",
      canVerify: true,
      verificationUrl: "/verify-payment-method",
    });
  }

  const txnId = `TXN-UCHI-2026-${Math.floor(100000 + Math.random() * 900000)}`;
  const code = "893201";
  otpStore[txnId] = { code, expiresAt: Date.now() + 10 * 60 * 1000, attempts: 0 };

  return res.json({
    status: "PAYMENT_OTP_PENDING",
    transactionId: txnId,
    amount: amount || 6200.0,
    currency: "USD",
    demoSecurityCode: code,
    message: "2FA authorization code dispatched to candidate email.",
  });
});

/**
 * 4. POST /api/payment/confirm-otp
 * Validates transaction OTP code and marks payment CONFIRMED
 */
paymentRouter.post("/confirm-otp", (req: Request, res: Response) => {
  const { transactionId, otp } = req.body || {};
  const entry = otpStore[transactionId];

  if (!entry || (otp !== entry.code && otp !== "893201")) {
    return res.status(400).json({ error: "Invalid or expired security code" });
  }

  const newTxn: TransactionRecord = {
    transactionId: transactionId || `TXN-UCHI-2026-89321`,
    invoiceNumber: `INV-UCHI-2026-89321`,
    approvalCode: `AUTH-UCHI-89321`,
    referenceNumber: `REF-UCHI-DEP-2027-6200`,
    amount: 6200.0,
    currency: "USD",
    status: "CONFIRMED",
    paymentMethod: "Discover Debit Card (•••• 0405)",
    cardLast4: "0405",
    cardBrand: "Discover Debit Card",
    completedTimestamp: new Date().toISOString(),
    student: defaultStudent,
    items: [
      {
        itemCode: "UC-CHEM-PHD-2027",
        description: "Ph.D. Matriculation Seat Locking & Enrollment Deposit — Cusumano Research Group",
        term: "Autumn 2027",
        amount: 6200.0,
      },
    ],
    subtotal: 6200.0,
    discount: 0.0,
    tax: 0.0,
    totalPaid: 6200.0,
  };

  transactionsStore.unshift(newTxn);
  delete otpStore[transactionId];

  return res.json({
    status: "CONFIRMED",
    transaction: newTxn,
    message: "Mandate cleared. Deposit successfully settled.",
  });
});

/**
 * 5. POST /api/payment/verification/request
 * Initiates pre-authorization card verification without CVV
 */
paymentRouter.post("/verification/request", (req: Request, res: Response) => {
  const { cardHolder, cardNumber, expiry, issuingBank, billingPostalCode, notificationEmail, cvv } = req.body || {};

  // Security rule: Never allow CVV on pre-authorization registration
  if (cvv) {
    return res.status(400).json({
      error: "CVV_FORBIDDEN",
      message: "In compliance with institutional clearing regulations, security CVV codes are never requested during pre-authorization registration.",
    });
  }

  const normalized = (cardNumber || "").replace(/\D/g, "");
  const requestId = `PVR-UCHI-${Math.floor(10000 + Math.random() * 90000)}`;
  const code = "893201";
  otpStore[requestId] = { code, expiresAt: Date.now() + 10 * 60 * 1000, attempts: 0 };

  return res.json({
    requestId,
    demoOtp: code,
    message: "Bursar security verification code dispatched.",
  });
});

/**
 * 6. POST /api/payment/verification/verify-otp
 * Verifies OTP and registers request with 15-20 days estimated period
 */
paymentRouter.post("/verification/verify-otp", (req: Request, res: Response) => {
  const { requestId, otp, cardHolder, cardNumber, expiry, issuingBank, billingPostalCode, notificationEmail } = req.body || {};
  const entry = otpStore[requestId];

  if (!entry || (otp !== entry.code && otp !== "893201")) {
    return res.status(400).json({ error: "Invalid or expired authorization code" });
  }

  const normalized = (cardNumber || "4000123456789010").replace(/\D/g, "");
  const last4 = normalized.slice(-4);
  const record: CardVerificationRequest = {
    requestId: requestId || `PVR-UCHI-89321`,
    cardHolder: cardHolder || "Devendra Dubey",
    cardNumberMasked: `•••• •••• •••• ${last4}`,
    last4,
    expiry: expiry || "04/32",
    issuingBank: issuingBank || "Stanford Federal Credit Union / Global Partner Bank",
    billingPostalCode: billingPostalCode || "421204",
    notificationEmail: notificationEmail || "devendra.dubey@iitgn.ac.in",
    status: "PENDING_VERIFICATION",
    submissionDate: new Date().toISOString(),
    estimatedReviewPeriod: "15 to 20 business days",
  };

  verificationRequestsStore.push(record);
  delete otpStore[requestId];

  return res.json({
    status: "PENDING_VERIFICATION",
    request: record,
    message: "Mandate pre-authorization request submitted. Review period: 15 to 20 business days.",
  });
});

/**
 * 7. POST /api/payment/verification/resend-otp
 */
paymentRouter.post("/verification/resend-otp", (req: Request, res: Response) => {
  const { requestId } = req.body || {};
  const code = "893201";
  otpStore[requestId] = { code, expiresAt: Date.now() + 10 * 60 * 1000, attempts: 0 };

  return res.json({
    success: true,
    demoOtp: code,
    message: "A new security code has been dispatched (cooldown active: 60s).",
  });
});

/**
 * 8. GET /api/payment/verification/list
 */
paymentRouter.get("/verification/list", (req: Request, res: Response) => {
  const { email } = req.query;
  if (email) {
    return res.json(verificationRequestsStore.filter((r) => r.notificationEmail === email));
  }
  return res.json(verificationRequestsStore);
});

/**
 * 9. POST /api/payment/verification/approve & reject
 */
paymentRouter.post("/verification/approve", (req: Request, res: Response) => {
  const { requestId, adminNotes } = req.body || {};
  const item = verificationRequestsStore.find((r) => r.requestId === requestId);
  if (!item) return res.status(404).json({ error: "Request not found" });

  item.status = "ADMIN_APPROVAL";
  item.adminNotes = adminNotes || "Approved by Bursar Clearing Desk.";

  verifiedCardsMap[item.last4] = {
    brand: "Approved Institutional Card",
    cardNumber: `••••••••••••${item.last4}`,
    maskedDisplay: item.cardNumberMasked,
    last4: item.last4,
    expiry: item.expiry,
    cardHolder: item.cardHolder,
    issuingBank: item.issuingBank,
    verificationDate: new Date().toISOString(),
    isVerified: true,
    preAuthStatus: "Verified & Pre-Authorized Mandate Active",
    designatedProgram: "Ph.D. Chemistry (Autumn 2027)",
  };

  return res.json({ success: true, item });
});

paymentRouter.post("/verification/reject", (req: Request, res: Response) => {
  const { requestId, adminNotes } = req.body || {};
  const item = verificationRequestsStore.find((r) => r.requestId === requestId);
  if (!item) return res.status(404).json({ error: "Request not found" });

  item.status = "REJECTED";
  item.adminNotes = adminNotes || "Mandate verification rejected.";
  return res.json({ success: true, item });
});

/**
 * 10. GET /api/payment/transactions
 */
paymentRouter.get("/transactions", (_req: Request, res: Response) => {
  return res.json(transactionsStore);
});

/**
 * 11. GET /api/payment/summary
 */
paymentRouter.get("/summary", (_req: Request, res: Response) => {
  const totalSpent = transactionsStore.reduce((acc, t) => acc + (t.status === "CONFIRMED" ? t.amount : 0), 0);
  return res.json({
    totalSpent,
    totalTransactions: transactionsStore.length,
    pendingVerifications: verificationRequestsStore.filter((r) => r.status === "PENDING_VERIFICATION").length,
    activeMandates: Object.keys(verifiedCardsMap).length,
  });
});

/**
 * 12. GET /api/payment/invoice/:id
 */
paymentRouter.get("/invoice/:id", (req: Request, res: Response) => {
  const txn = transactionsStore.find((t) => t.transactionId === req.params.id || t.invoiceNumber === req.params.id) || transactionsStore[0];
  const receipt: ReceiptData = {
    organization: "The University of Chicago",
    association: "Office of the Bursar & Student Accounts",
    unit: "Division of the Physical Sciences • Dept. of Chemistry",
    address: "Searle Chemistry Laboratories • 5801 S. Ellis Avenue, Chicago, IL 60637 USA",
    contactEmail: "bursar@uchicago.asia",
    website: "https://uchicago.edu",
    taxYear: "2026–2027",
    form1098Eligible: true,
    transaction: txn,
  };
  return res.json(receipt);
});

/**
 * 13. GET /api/payment/invoice/:id/download & /pdf
 */
paymentRouter.get(["/invoice/:id/download", "/invoice/:id/pdf"], (req: Request, res: Response) => {
  const isAppFee = req.params.id && (req.params.id.includes("APP") || req.params.id.includes("100101") || req.params.id === "90");
  const fileName = isAppFee ? "Official_Application_Fee_Receipt_UCHI_2026.pdf" : "Official_Receipt_UCHI_2027_6200.pdf";
  const pdfPath = path.resolve(__dirname, `../site_1to1/assets/documents/${fileName}`);
  if (fs.existsSync(pdfPath)) {
    res.setHeader("Content-Type", "application/pdf");
    res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
    return fs.createReadStream(pdfPath).pipe(res);
  }
  return res.status(404).json({ error: "PDF not found" });
});

/**
 * 14. POST /api/payment/invoice/:id/resend-email
 */
paymentRouter.post("/invoice/:id/resend-email", (req: Request, res: Response) => {
  return res.json({
    success: true,
    message: "Official A4 Tax Invoice dispatched to devendra.dubey@iitgn.ac.in",
  });
});
