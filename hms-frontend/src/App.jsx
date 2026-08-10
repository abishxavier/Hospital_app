import { Activity, ArrowRight, BedDouble, BellRing, CalendarClock, CircleDollarSign, HeartPulse, LayoutGrid, Search, Settings, Sparkles, Stethoscope, Users2 } from 'lucide-react';
import { Bar, BarChart, CartesianGrid, Cell, Line, LineChart, Pie, PieChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

const sidebarItems = [
  { name: 'Overview', icon: LayoutGrid, active: true },
  { name: 'Patients', icon: Users2 },
  { name: 'Appointments', icon: CalendarClock },
  { name: 'Doctors', icon: Stethoscope },
  { name: 'Beds', icon: BedDouble },
  { name: 'Billing', icon: CircleDollarSign },
];

const metrics = [
  { label: 'Admissions', value: '1,248', detail: '+12% vs last month', tint: 'from-cyan-500 to-blue-600' },
  { label: 'ICU Occupancy', value: '82%', detail: '3 critical beds active', tint: 'from-fuchsia-500 to-violet-600' },
  { label: 'Revenue', value: '₹18.4L', detail: 'Collected this week', tint: 'from-emerald-500 to-teal-600' },
  { label: 'Avg. Wait Time', value: '14 min', detail: 'Improved by 6 mins', tint: 'from-amber-500 to-orange-600' },
];

const flowData = [
  { name: 'Mon', patients: 54, revenue: 130 },
  { name: 'Tue', patients: 66, revenue: 155 },
  { name: 'Wed', patients: 58, revenue: 148 },
  { name: 'Thu', patients: 74, revenue: 182 },
  { name: 'Fri', patients: 71, revenue: 168 },
  { name: 'Sat', patients: 89, revenue: 220 },
];

const serviceMix = [
  { name: 'OPD', value: 40, color: '#2563eb' },
  { name: 'IPD', value: 28, color: '#14b8a6' },
  { name: 'Lab', value: 20, color: '#f59e0b' },
  { name: 'Pharma', value: 12, color: '#8b5cf6' },
];

const appointments = [
  { time: '09:30', patient: 'Aarav Kumar', doctor: 'Dr. Nair', status: 'Confirmed' },
  { time: '11:00', patient: 'Meera Shah', doctor: 'Dr. Rao', status: 'In Review' },
  { time: '01:15', patient: 'Ravi Joshi', doctor: 'Dr. Sinha', status: 'New' },
];

function StatCard({ label, value, detail, tint }) {
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

export default function App() {
  return (
    <div className="min-h-screen bg-[radial-gradient(circle_at_top_left,_rgba(56,189,248,0.18),_transparent_35%),linear-gradient(135deg,_#f8fbff_0%,_#eef4ff_100%)] p-4 text-slate-800 lg:p-6">
      <div className="mx-auto flex min-h-[calc(100vh-2rem)] max-w-7xl flex-col overflow-hidden rounded-[32px] border border-white/70 bg-white/80 shadow-[0_30px_90px_rgba(15,23,42,0.14)] backdrop-blur xl:flex-row">
        <aside className="w-full bg-slate-950 p-6 text-white xl:w-72">
          <div className="flex items-center gap-3">
            <div className="rounded-2xl bg-cyan-500/20 p-2 text-cyan-300">
              <HeartPulse className="h-6 w-6" />
            </div>
            <div>
              <p className="text-lg font-semibold">HMS Control</p>
              <p className="text-sm text-slate-400">Care operations hub</p>
            </div>
          </div>

          <nav className="mt-8 space-y-2">
            {sidebarItems.map(({ name, icon: Icon, active }) => (
              <button key={name} className={`flex w-full items-center justify-between rounded-2xl px-3 py-3 text-left text-sm transition ${active ? 'bg-cyan-500/20 text-cyan-200' : 'text-slate-300 hover:bg-slate-800'}`}>
                <span className="flex items-center gap-3">
                  <Icon className="h-4 w-4" />
                  {name}
                </span>
                {active ? <Sparkles className="h-4 w-4" /> : null}
              </button>
            ))}
          </nav>

          <div className="mt-8 rounded-3xl border border-slate-800 bg-slate-900/80 p-4">
            <div className="flex items-center gap-2 text-sm font-medium text-cyan-300">
              <Activity className="h-4 w-4" />
              Live status
            </div>
            <p className="mt-2 text-2xl font-semibold">24/7</p>
            <p className="text-sm text-slate-400">Emergency response and ward coverage active.</p>
          </div>
        </aside>

        <main className="flex-1 bg-slate-50/80 p-4 lg:p-6">
          <header className="rounded-[28px] bg-gradient-to-br from-slate-900 via-slate-800 to-cyan-700 p-6 text-white shadow-lg">
            <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
              <div>
                <p className="text-sm uppercase tracking-[0.3em] text-cyan-200">Hospital overview</p>
                <h1 className="mt-2 text-3xl font-semibold">Welcome back, Dr. Sharma</h1>
                <p className="mt-2 text-sm text-slate-300">A polished command center for admissions, appointments, and care delivery.</p>
              </div>
              <div className="flex items-center gap-3 rounded-2xl border border-white/15 bg-white/10 px-4 py-3 backdrop-blur">
                <Search className="h-4 w-4 text-cyan-200" />
                <input className="w-40 bg-transparent text-sm outline-none placeholder:text-slate-300" placeholder="Search patient" />
              </div>
            </div>
          </header>

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
                  <p className="text-sm text-slate-500">Today’s queue with priority care follow-up</p>
                </div>
                <button className="inline-flex items-center gap-2 rounded-full bg-slate-900 px-3 py-2 text-sm font-medium text-white">
                  View all <ArrowRight className="h-4 w-4" />
                </button>
              </div>
              <div className="mt-4 space-y-3">
                {appointments.map((item) => (
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
        </main>
      </div>
    </div>
  );
}
