export default function StatCard({ label, value, detail, tint }) {
  return (
    <div className={`rounded-[24px] bg-gradient-to-br ${tint} p-[1px] shadow-lg`}>
      <div className="rounded-[23px] bg-slate-950/95 p-5 text-white">
        <p className="text-sm text-slate-300">{label}</p>
        <p className="mt-2 text-3xl font-semibold">{value}</p>
        <p className="mt-1 text-sm text-slate-400">{detail}</p>
      </div>
    </div>
  );
}
