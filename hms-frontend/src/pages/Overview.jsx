import { ArrowRight, BellRing, Settings } from 'lucide-react';
import { Link } from 'react-router-dom';
import { Bar, BarChart, CartesianGrid, Cell, Line, LineChart, Pie, PieChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import PageHeader from '../components/PageHeader';
import StatCard from '../components/StatCard';
import { appointments, flowData, metrics, serviceMix } from '../data/mockData';

export default function Overview() {
  return (
    <>
      <PageHeader
        eyebrow="Hospital overview"
        title="Welcome back, Dr. Sharma"
        subtitle="A polished command center for admissions, appointments, and care delivery."
        searchPlaceholder="Search patient"
      />

      <section className="mt-6 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        {metrics.map((metric) => (
          <StatCard key={metric.label} {...metric} />
        ))}
      </section>

      <section className="mt-6 grid gap-6 xl:grid-cols-[1.3fr_0.7fr]">
        <div className="rounded-[28px] border border-slate-200 bg-white p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-lg font-semibold text-slate-900">Weekly patient flow</h2>
              <p className="text-sm text-slate-500">A steady rise in visits and revenue this week</p>
            </div>
            <button className="rounded-full bg-slate-100 p-2 text-slate-600">
              <Settings className="h-4 w-4" />
            </button>
          </div>
          <div className="mt-4 h-72">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={flowData}>
                <CartesianGrid stroke="#e2e8f0" strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="patients" stroke="#2563eb" strokeWidth={3} />
                <Line type="monotone" dataKey="revenue" stroke="#14b8a6" strokeWidth={3} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="rounded-[28px] border border-slate-200 bg-white p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold text-slate-900">Service mix</h2>
            <span className="rounded-full bg-cyan-50 px-3 py-1 text-sm font-medium text-cyan-600">Balanced</span>
          </div>
          <div className="mt-4 h-72">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie data={serviceMix} dataKey="value" nameKey="name" innerRadius={70} outerRadius={110} paddingAngle={3}>
                  {serviceMix.map((entry) => (
                    <Cell key={entry.name} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>
      </section>

      <section className="mt-6 grid gap-6 xl:grid-cols-[1.05fr_0.95fr]">
        <div className="rounded-[28px] border border-slate-200 bg-white p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-lg font-semibold text-slate-900">Upcoming appointments</h2>
              <p className="text-sm text-slate-500">Today's queue with priority care follow-up</p>
            </div>
            <Link to="/appointments" className="inline-flex items-center gap-2 rounded-full bg-slate-900 px-3 py-2 text-sm font-medium text-white">
              View all <ArrowRight className="h-4 w-4" />
            </Link>
          </div>
          <div className="mt-4 space-y-3">
            {appointments.slice(0, 3).map((item) => (
              <div key={item.time} className="flex items-center justify-between rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3">
                <div>
                  <p className="font-medium text-slate-900">{item.patient}</p>
                  <p className="text-sm text-slate-500">{item.doctor}</p>
                </div>
                <div className="text-right">
                  <p className="rounded-full bg-cyan-50 px-3 py-1 text-sm font-medium text-cyan-700">{item.time}</p>
                  <p className="mt-1 text-xs text-slate-500">{item.status}</p>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="rounded-[28px] border border-slate-200 bg-white p-5 shadow-sm">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-lg font-semibold text-slate-900">Care priorities</h2>
              <p className="text-sm text-slate-500">Operational focus for the next shift</p>
            </div>
            <div className="rounded-full bg-amber-100 p-2 text-amber-700">
              <BellRing className="h-4 w-4" />
            </div>
          </div>

          <div className="mt-4 space-y-4">
            <div className="rounded-2xl bg-slate-900 p-4 text-white">
              <div className="flex items-center justify-between">
                <p className="text-sm text-slate-300">Critical alerts</p>
                <p className="text-2xl font-semibold">4</p>
              </div>
              <p className="mt-2 text-sm text-slate-400">High priority cases needs immediate review.</p>
            </div>

            <div className="rounded-2xl border border-slate-200 p-4">
              <div className="flex items-center justify-between">
                <span className="text-sm font-medium text-slate-700">Bed readiness</span>
                <span className="text-sm font-semibold text-emerald-600">87%</span>
              </div>
              <div className="mt-2 h-2 rounded-full bg-slate-200">
                <div className="h-2 w-[87%] rounded-full bg-gradient-to-r from-emerald-500 to-cyan-500" />
              </div>
            </div>

            <div className="rounded-2xl border border-slate-200 p-4">
              <div className="flex items-center justify-between">
                <span className="text-sm font-medium text-slate-700">Lab turnaround</span>
                <span className="text-sm font-semibold text-blue-600">76%</span>
              </div>
              <div className="mt-2 h-2 rounded-full bg-slate-200">
                <div className="h-2 w-[76%] rounded-full bg-gradient-to-r from-blue-500 to-violet-500" />
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
