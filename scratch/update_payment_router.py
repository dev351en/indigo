import os

with open('server/paymentRouter.ts', 'r', encoding='utf-8') as f:
    text = f.read()

app_fee_txn = '''  {
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
  },'''

if 'TXN-UCHI-APP-2026-100101' not in text:
    anchor = 'export const transactionsStore: TransactionRecord[] = ['
    text = text.replace(anchor, anchor + '\n' + app_fee_txn, 1)
    print('Added app fee txn to transactionsStore')

old_download = '''paymentRouter.get(["/invoice/:id/download", "/invoice/:id/pdf"], (_req: Request, res: Response) => {
  const pdfPath = path.resolve(__dirname, "../site_1to1/assets/documents/Official_Receipt_UCHI_2027_6200.pdf");
  if (fs.existsSync(pdfPath)) {
    res.setHeader("Content-Type", "application/pdf");
    res.setHeader("Content-Disposition", 'attachment; filename="Official_Receipt_UCHI_2027_6200.pdf"');
    return fs.createReadStream(pdfPath).pipe(res);
  }
  return res.status(404).json({ error: "PDF not found" });
});'''

new_download = '''paymentRouter.get(["/invoice/:id/download", "/invoice/:id/pdf"], (req: Request, res: Response) => {
  const isAppFee = req.params.id && (req.params.id.includes("APP") || req.params.id.includes("100101") || req.params.id === "90");
  const fileName = isAppFee ? "Official_Application_Fee_Receipt_UCHI_2026.pdf" : "Official_Receipt_UCHI_2027_6200.pdf";
  const pdfPath = path.resolve(__dirname, `../site_1to1/assets/documents/${fileName}`);
  if (fs.existsSync(pdfPath)) {
    res.setHeader("Content-Type", "application/pdf");
    res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
    return fs.createReadStream(pdfPath).pipe(res);
  }
  return res.status(404).json({ error: "PDF not found" });
});'''

text = text.replace(old_download, new_download)

with open('server/paymentRouter.ts', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated server/paymentRouter.ts successfully!')
