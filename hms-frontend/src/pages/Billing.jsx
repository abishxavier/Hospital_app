import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import { FileText } from 'lucide-react';
import PageHeader from '../components/PageHeader';
import StatCard from '../components/StatCard';
import { invoices, revenueByDept } from '../data/mockData';

const statusStyles = {
  Paid: 'bg-emerald-50 text-emerald-700',
  Pending: 'bg-amber-50 text-amber-700',
  Overdue: 'bg-red-50 text-red-700',
};

function formatINR(amount) {
  return `₹${amount.toLocaleString('en-IN')}`;
}

export default function Billing() {
  const totalCollected = invoices.filter((i) => i.status === 'Paid').reduce((s, i) => s + i.amount, 0);
  const totalPending = invoices.filter((i) => i.status !== 'Paid').reduce((s, i) => s + i.amount, 0);

  const summary = [
    { label: 'Collected', value: formatINR(totalCollected), detail: 'Across paid invoices', tint: 'from-emerald-500 to-teal-600' },
    { label: 'Outstanding', value: formatINR(totalPending), detail: 'Pending + overdue', tint: 'from-amber-500 to-orange-600' },
    { label: 'Invoices', value: String(invoices.length), detail: 'Generated this week', tint: 'from-cyan-500 to-blue-600' },
  ];

  return (
    <>
      <PageHeader eyebrow="Finance" title="Billing" subtitle="Track invoices, collections, and department revenue" />

      <section className="mt-6 grid gap-4 md:grid-cols-3">
        {summary.map((s) => (
          <StatCard key={s.label} {...s} />
        ))}
      </section>

      <section className="mt-6 grid gap-6 xl:grid-cols-[0.9fr_1.1fr]">
        <div className="rounded-[28px] border border-slate-200 bg-white p-5 shadow-sm">
          <h2 className="text-lg font-semibold text-slate-900">Revenue by department</h2>
          <p className="text-sm text-slate-500">This month, in ₹</p>
          <div className="mt-4 h-64">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={revenueByDept}>
                <CartesianGrid stroke="#e2e8f0" strokeDasharray="3 3" />
                <XAxis dataKey="name" tick={{ fontSize: 11 }} interval={0} angle={-15} textAnchor="end" height={50} />
                <YAxis tickFormatter={(v) => `${v / 1000}k`} />
                <Tooltip formatter={(v) => formatINR(v)} />
                <Bar dataKey="value" fill="#0891b2" radius={[6, 6, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="rounded-[28px] border border-slate-200 bg-white p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold text-slate-900">Recent invoices</h2>
            <FileText className="h-4 w-4 text-slate-400" />
          </div>
          <div className="mt-4 overflow-x-auto">
            <table className="w-full min-w-[480px] border-collapse text-left text-sm">
              <thead>
                <tr className="text-xs uppercase tracking-wide text-slate-400">
                  <th className="pb-3 pr-4">Invoice</th>
                  <th className="pb-3 pr-4">Patient</th>
                  <th className="pb-3 pr-4">Amount</th>
                  <th className="pb-3">Status</th>
                </tr>
              </thead>
              <tbody>
                {invoices.map((inv) => (
                  <tr key={inv.id} className="border-t border-slate-100">
                    <td className="py-3 pr-4">
                      <p className="font-medium text-slate-900">{inv.id}</p>
                      <p className="text-xs text-slate-400">{inv.date}</p>
                    </td>
                    <td className="py-3 pr-4 text-slate-600">{inv.patient}</td>
                    <td className="py-3 pr-4 text-slate-600">{formatINR(inv.amount)}</td>
                    <td className="py-3">
                      <span className={`rounded-full px-3 py-1 text-xs font-medium ${statusStyles[inv.status] || 'bg-slate-100 text-slate-700'}`}>
                        {inv.status}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </>
  );
}
