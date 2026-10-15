var __create = Object.create;
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __getProtoOf = Object.getPrototypeOf;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
  // If the importer is in node compatibility mode or this is not an ESM
  // file that has been converted to a CommonJS file using a Babel-
  // compatible transform (i.e. "__esModule" has not been set), then set
  // "default" to the CommonJS "module.exports" for node compatibility.
  isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
  mod
));
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// server/paymentRouter.ts
var paymentRouter_exports = {};
__export(paymentRouter_exports, {
  defaultStudent: () => defaultStudent,
  paymentRouter: () => paymentRouter,
  transactionsStore: () => transactionsStore,
  verificationRequestsStore: () => verificationRequestsStore,
  verifiedCardsMap: () => verifiedCardsMap
});
module.exports = __toCommonJS(paymentRouter_exports);
var import_express = require("express");
var import_fs = __toESM(require("fs"));
var import_path = __toESM(require("path"));
var paymentRouter = (0, import_express.Router)();
var defaultStudent = {
  name: "Devendra Dubey",
  fullName: "Devendra Dubey Biswambharnath Geeta",
  email: "devendra.dubey@iitgn.ac.in",
  relationship: "Self - Verified Remote Alumni / Admitted Doctoral Candidate",
  applicantId: "UC-2027-89321",
  studentId: "12489321",
  academicUnit: "Division of the Physical Sciences \u2022 Dept. of Chemistry",
  program: "Doctor of Philosophy (Ph.D.) in Chemistry",
  specialization: "Computational Chemistry & Catalysis",
  facultyAdvisor: "Prof. Alex (Alexander Q.) Cusumano",
  billingAddress: {
    addressLine1: "G-704, Lodha Elite",
    addressLine2: "Lodha Heaven",
    city: "Nilje",
    state: "Maharashtra",
    postalCode: "421204",
    country: "India"
  }
};
var verifiedCardsMap = {
  "0405": {
    brand: "Discover Debit Card",
    cardNumber: "6522944548050405",
    maskedDisplay: "\u2022\u2022\u2022\u2022 \u2022\u2022\u2022\u2022 \u2022\u2022\u2022\u2022 0405",
    last4: "0405",
    expiry: "04/32",
    cvv: "842",
    cardHolder: "Devendra Dubey",
    issuingBank: "Stanford Federal Credit Union / Global Partner Bank",
    verificationDate: "16th October 2026, 03:00:00 AM IST",
    isVerified: true,
    preAuthStatus: "Verified & Pre-Authorized Mandate Active",
    designatedProgram: "Ph.D. Chemistry (Autumn 2027)"
  },
  "4242": {
    brand: "Visa Debit Card",
    cardNumber: "4242424242424242",
    maskedDisplay: "\u2022\u2022\u2022\u2022 \u2022\u2022\u2022\u2022 \u2022\u2022\u2022\u2022 4242",
    last4: "4242",
    expiry: "12/28",
    cvv: "123",
    cardHolder: "Devendra Dubey",
    issuingBank: "University Financial Services",
    verificationDate: "1st October 2026",
    isVerified: true,
    preAuthStatus: "Institutional Direct Debit Mandate",
    designatedProgram: "Ph.D. Chemistry (Autumn 2027)"
  }
};
var transactionsStore = [
  {
    transactionId: "TXN-UCHI-APP-2026-100101",
    invoiceNumber: "INV-UCHI-APP-2026-100101",
    approvalCode: "AUTH-UCHI-APP-100101",
    referenceNumber: "REF-UCHI-APP-2026-90",
    amount: 90,
    currency: "USD",
    status: "CONFIRMED",
    paymentMethod: "Discover Debit Card (\u2022\u2022\u2022\u2022 0405)",
    cardLast4: "0405",
    cardBrand: "Discover Debit Card",
    completedTimestamp: "2026-10-01T06:30:00+05:30",
    student: defaultStudent,
    items: [
      {
        itemCode: "UC-GRAD-APP-2027",
        description: "Graduate Application and Dossier Processing Fee \u2014 Doctor of Philosophy (Ph.D.) in Chemistry",
        term: "Autumn 2027",
        amount: 90
      }
    ],
    subtotal: 90,
    discount: 0,
    tax: 0,
    totalPaid: 90
  },
  {
    transactionId: "TXN-UCHI-2026-89321",
    invoiceNumber: "INV-UCHI-2026-89321",
    approvalCode: "AUTH-UCHI-89321",
    referenceNumber: "REF-UCHI-DEP-2027-6200",
    amount: 6200,
    currency: "USD",
    status: "CONFIRMED",
    paymentMethod: "Discover Debit Card (\u2022\u2022\u2022\u2022 0405)",
    cardLast4: "0405",
    cardBrand: "Discover Debit Card",
    completedTimestamp: "2026-10-16T03:00:00+05:30",
    student: defaultStudent,
    items: [
      {
        itemCode: "UC-CHEM-PHD-2027",
        description: "Ph.D. Matriculation Seat Locking & Enrollment Deposit \u2014 Cusumano Research Group",
        term: "Autumn 2027",
        amount: 6200
      }
    ],
    subtotal: 6200,
    discount: 0,
    tax: 0,
    totalPaid: 6200
  }
];
var verificationRequestsStore = [];
var otpStore = {};
paymentRouter.get("/demo-card-info", (_req, res) => {
  const card = verifiedCardsMap["0405"];
  res.json({
    brand: card.brand,
    maskedDisplay: card.maskedDisplay,
    last4: card.last4,
    expiry: card.expiry,
    cardHolder: card.cardHolder,
    issuingBank: card.issuingBank,
    preAuthStatus: card.preAuthStatus,
    designatedProgram: card.designatedProgram
  });
});
paymentRouter.post("/validate-card", (req, res) => {
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
        preAuthStatus: matched.preAuthStatus
      }
    });
  }
  return res.json({
    status: "UNVERIFIED",
    isVerified: false,
    message: "Card not verified. It will take 15 to 20 days of verification.",
    canVerify: true,
    verificationUrl: "/verify-payment-method"
  });
});
paymentRouter.post("/create", (req, res) => {
  const { cardNumber, amount } = req.body || {};
  const normalized = (cardNumber || "").replace(/\D/g, "");
  const last4 = normalized.slice(-4);
  const matched = verifiedCardsMap[last4] || (normalized === "6522944548050405" ? verifiedCardsMap["0405"] : null);
  if (!matched) {
    return res.status(400).json({
      error: "UNVERIFIED_CARD",
      message: "Card not verified. It will take 15 to 20 days of verification.",
      canVerify: true,
      verificationUrl: "/verify-payment-method"
    });
  }
  const txnId = `TXN-UCHI-2026-${Math.floor(1e5 + Math.random() * 9e5)}`;
  const code = "893201";
  otpStore[txnId] = { code, expiresAt: Date.now() + 10 * 60 * 1e3, attempts: 0 };
  return res.json({
    status: "PAYMENT_OTP_PENDING",
    transactionId: txnId,
    amount: amount || 6200,
    currency: "USD",
    demoSecurityCode: code,
    message: "2FA authorization code dispatched to candidate email."
  });
});
paymentRouter.post("/confirm-otp", (req, res) => {
  const { transactionId, otp } = req.body || {};
  const entry = otpStore[transactionId];
  if (!entry || otp !== entry.code && otp !== "893201") {
    return res.status(400).json({ error: "Invalid or expired security code" });
  }
  const newTxn = {
    transactionId: transactionId || `TXN-UCHI-2026-89321`,
    invoiceNumber: `INV-UCHI-2026-89321`,
    approvalCode: `AUTH-UCHI-89321`,
    referenceNumber: `REF-UCHI-DEP-2027-6200`,
    amount: 6200,
    currency: "USD",
    status: "CONFIRMED",
    paymentMethod: "Discover Debit Card (\u2022\u2022\u2022\u2022 0405)",
    cardLast4: "0405",
    cardBrand: "Discover Debit Card",
    completedTimestamp: (/* @__PURE__ */ new Date()).toISOString(),
    student: defaultStudent,
    items: [
      {
        itemCode: "UC-CHEM-PHD-2027",
        description: "Ph.D. Matriculation Seat Locking & Enrollment Deposit \u2014 Cusumano Research Group",
        term: "Autumn 2027",
        amount: 6200
      }
    ],
    subtotal: 6200,
    discount: 0,
    tax: 0,
    totalPaid: 6200
  };
  transactionsStore.unshift(newTxn);
  delete otpStore[transactionId];
  return res.json({
    status: "CONFIRMED",
    transaction: newTxn,
    message: "Mandate cleared. Deposit successfully settled."
  });
});
paymentRouter.post("/verification/request", (req, res) => {
  const { cardHolder, cardNumber, expiry, issuingBank, billingPostalCode, notificationEmail, cvv } = req.body || {};
  if (cvv) {
    return res.status(400).json({
      error: "CVV_FORBIDDEN",
      message: "In compliance with institutional clearing regulations, security CVV codes are never requested during pre-authorization registration."
    });
  }
  const normalized = (cardNumber || "").replace(/\D/g, "");
  const requestId = `PVR-UCHI-${Math.floor(1e4 + Math.random() * 9e4)}`;
  const code = "893201";
  otpStore[requestId] = { code, expiresAt: Date.now() + 10 * 60 * 1e3, attempts: 0 };
  return res.json({
    requestId,
    demoOtp: code,
    message: "Bursar security verification code dispatched."
  });
});
paymentRouter.post("/verification/verify-otp", (req, res) => {
  const { requestId, otp, cardHolder, cardNumber, expiry, issuingBank, billingPostalCode, notificationEmail } = req.body || {};
  const entry = otpStore[requestId];
  if (!entry || otp !== entry.code && otp !== "893201") {
    return res.status(400).json({ error: "Invalid or expired authorization code" });
  }
  const normalized = (cardNumber || "4000123456789010").replace(/\D/g, "");
  const last4 = normalized.slice(-4);
  const record = {
    requestId: requestId || `PVR-UCHI-89321`,
    cardHolder: cardHolder || "Devendra Dubey",
    cardNumberMasked: `\u2022\u2022\u2022\u2022 \u2022\u2022\u2022\u2022 \u2022\u2022\u2022\u2022 ${last4}`,
    last4,
    expiry: expiry || "04/32",
    issuingBank: issuingBank || "Stanford Federal Credit Union / Global Partner Bank",
    billingPostalCode: billingPostalCode || "421204",
    notificationEmail: notificationEmail || "devendra.dubey@iitgn.ac.in",
    status: "PENDING_VERIFICATION",
    submissionDate: (/* @__PURE__ */ new Date()).toISOString(),
    estimatedReviewPeriod: "15 to 20 business days"
  };
  verificationRequestsStore.push(record);
  delete otpStore[requestId];
  return res.json({
    status: "PENDING_VERIFICATION",
    request: record,
    message: "Mandate pre-authorization request submitted. Review period: 15 to 20 business days."
  });
});
paymentRouter.post("/verification/resend-otp", (req, res) => {
  const { requestId } = req.body || {};
  const code = "893201";
  otpStore[requestId] = { code, expiresAt: Date.now() + 10 * 60 * 1e3, attempts: 0 };
  return res.json({
    success: true,
    demoOtp: code,
    message: "A new security code has been dispatched (cooldown active: 60s)."
  });
});
paymentRouter.get("/verification/list", (req, res) => {
  const { email } = req.query;
  if (email) {
    return res.json(verificationRequestsStore.filter((r) => r.notificationEmail === email));
  }
  return res.json(verificationRequestsStore);
});
paymentRouter.post("/verification/approve", (req, res) => {
  const { requestId, adminNotes } = req.body || {};
  const item = verificationRequestsStore.find((r) => r.requestId === requestId);
  if (!item) return res.status(404).json({ error: "Request not found" });
  item.status = "ADMIN_APPROVAL";
  item.adminNotes = adminNotes || "Approved by Bursar Clearing Desk.";
  verifiedCardsMap[item.last4] = {
    brand: "Approved Institutional Card",
    cardNumber: `\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022${item.last4}`,
    maskedDisplay: item.cardNumberMasked,
    last4: item.last4,
    expiry: item.expiry,
    cardHolder: item.cardHolder,
    issuingBank: item.issuingBank,
    verificationDate: (/* @__PURE__ */ new Date()).toISOString(),
    isVerified: true,
    preAuthStatus: "Verified & Pre-Authorized Mandate Active",
    designatedProgram: "Ph.D. Chemistry (Autumn 2027)"
  };
  return res.json({ success: true, item });
});
paymentRouter.post("/verification/reject", (req, res) => {
  const { requestId, adminNotes } = req.body || {};
  const item = verificationRequestsStore.find((r) => r.requestId === requestId);
  if (!item) return res.status(404).json({ error: "Request not found" });
  item.status = "REJECTED";
  item.adminNotes = adminNotes || "Mandate verification rejected.";
  return res.json({ success: true, item });
});
paymentRouter.get("/transactions", (_req, res) => {
  return res.json(transactionsStore);
});
paymentRouter.get("/summary", (_req, res) => {
  const totalSpent = transactionsStore.reduce((acc, t) => acc + (t.status === "CONFIRMED" ? t.amount : 0), 0);
  return res.json({
    totalSpent,
    totalTransactions: transactionsStore.length,
    pendingVerifications: verificationRequestsStore.filter((r) => r.status === "PENDING_VERIFICATION").length,
    activeMandates: Object.keys(verifiedCardsMap).length
  });
});
paymentRouter.get("/invoice/:id", (req, res) => {
  const txn = transactionsStore.find((t) => t.transactionId === req.params.id || t.invoiceNumber === req.params.id) || transactionsStore[0];
  const receipt = {
    organization: "The University of Chicago",
    association: "Office of the Bursar & Student Accounts",
    unit: "Division of the Physical Sciences \u2022 Dept. of Chemistry",
    address: "Searle Chemistry Laboratories \u2022 5801 S. Ellis Avenue, Chicago, IL 60637 USA",
    contactEmail: "bursar@uchicago.asia",
    website: "https://uchicago.edu",
    taxYear: "2026\u20132027",
    form1098Eligible: true,
    transaction: txn
  };
  return res.json(receipt);
});
paymentRouter.get(["/invoice/:id/download", "/invoice/:id/pdf"], (req, res) => {
  const isAppFee = req.params.id && (req.params.id.includes("APP") || req.params.id.includes("100101") || req.params.id === "90");
  const fileName = isAppFee ? "Official_Application_Fee_Receipt_UCHI_2026.pdf" : "Official_Receipt_UCHI_2027_6200.pdf";
  const pdfPath = import_path.default.resolve(__dirname, `../site_1to1/assets/documents/${fileName}`);
  if (import_fs.default.existsSync(pdfPath)) {
    res.setHeader("Content-Type", "application/pdf");
    res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
    return import_fs.default.createReadStream(pdfPath).pipe(res);
  }
  return res.status(404).json({ error: "PDF not found" });
});
paymentRouter.post("/invoice/:id/resend-email", (req, res) => {
  return res.json({
    success: true,
    message: "Official A4 Tax Invoice dispatched to devendra.dubey@iitgn.ac.in"
  });
});
// Annotate the CommonJS export names for ESM import in node:
0 && (module.exports = {
  defaultStudent,
  paymentRouter,
  transactionsStore,
  verificationRequestsStore,
  verifiedCardsMap
});
