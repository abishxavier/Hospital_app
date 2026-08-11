import { BedDouble } from 'lucide-react';
import PageHeader from '../components/PageHeader';
import { wards } from '../data/mockData';

function occupancyTint(pct) {
  if (pct >= 85) return 'from-red-500 to-orange-500';
  if (pct >= 65) return 'from-amber-500 to-orange-400';
  return 'from-emerald-500 to-cyan-500';
}

export default function Beds() {
  const totalBeds = wards.reduce((sum, w) => sum + w.total, 0);
  const totalOccupied = wards.reduce((sum, w) => sum + w.occupied, 0);
  const overallPct = Math.round((totalOccupied / totalBeds) * 100);

  return (
    <>
      <PageHeader
        eyebrow="Bed management"
        title="Beds"
        subtitle={`${totalOccupied} of ${totalBeds} beds occupied hospital-wide (${overallPct}%)`}
      />

      <section className="mt-6 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
        {wards.map((w) => {
          const pct = Math.round((w.occupied / w.total) * 100);
          return (
            <div key={w.name} className="rounded-[24px] border border-slate-200 bg-white p-5 shadow-sm">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="rounded-2xl bg-slate-100 p-2.5 text-slate-600">
                    <BedDouble className="h-5 w-5" />
                  </div>
                  <div>
                    <p className="font-medium text-slate-900">{w.name}</p>
                    <p className="text-sm text-slate-500">{w.occupied} / {w.total} beds occupied</p>
                  </div>
                </div>
                <span className="text-lg font-semibold text-slate-900">{pct}%</span>
              </div>
              <div className="mt-4 h-2 rounded-full bg-slate-200">
                <div className={`h-2 rounded-full bg-gradient-to-r ${occupancyTint(pct)}`} style={{ width: `${pct}%` }} />
              </div>
              <p className="mt-2 text-xs text-slate-400">{w.total - w.occupied} beds available</p>
            </div>
          );
        })}
      </section>
    </>
  );
}
