import { Stethoscope, Users2 } from 'lucide-react';
import PageHeader from '../components/PageHeader';
import { doctors } from '../data/mockData';

const statusStyles = {
  Available: 'bg-emerald-50 text-emerald-700',
  'In Consult': 'bg-amber-50 text-amber-700',
  'On Rounds': 'bg-cyan-50 text-cyan-700',
  'Off Duty': 'bg-slate-100 text-slate-500',
};

export default function Doctors() {
  return (
    <>
      <PageHeader
        eyebrow="Care team"
        title="Doctors"
        subtitle={`${doctors.length} doctors on staff today across all departments`}
      />

      <section className="mt-6 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
        {doctors.map((doc) => (
          <div key={doc.name} className="rounded-[24px] border border-slate-200 bg-white p-5 shadow-sm">
            <div className="flex items-start justify-between">
              <div className="flex items-center gap-3">
                <div className="rounded-2xl bg-cyan-50 p-2.5 text-cyan-600">
                  <Stethoscope className="h-5 w-5" />
                </div>
                <div>
                  <p className="font-medium text-slate-900">{doc.name}</p>
                  <p className="text-sm text-slate-500">{doc.specialty}</p>
                </div>
              </div>
              <span className={`rounded-full px-3 py-1 text-xs font-medium ${statusStyles[doc.status] || 'bg-slate-100 text-slate-700'}`}>
                {doc.status}
              </span>
            </div>

            <div className="mt-4 flex items-center justify-between rounded-2xl bg-slate-50 px-4 py-3">
              <div className="flex items-center gap-2 text-sm text-slate-600">
                <Users2 className="h-4 w-4" />
                Patients today
              </div>
              <span className="font-semibold text-slate-900">{doc.patientsToday}</span>
            </div>

            <p className="mt-3 text-xs text-slate-400">{doc.experience} experience</p>
          </div>
        ))}
      </section>
    </>
  );
}
