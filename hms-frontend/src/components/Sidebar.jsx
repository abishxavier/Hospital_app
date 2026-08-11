import { NavLink } from 'react-router-dom';
import { Activity, BedDouble, CalendarClock, CircleDollarSign, HeartPulse, LayoutGrid, Sparkles, Stethoscope, Users2 } from 'lucide-react';

const sidebarItems = [
  { name: 'Overview', to: '/', icon: LayoutGrid },
  { name: 'Patients', to: '/patients', icon: Users2 },
  { name: 'Appointments', to: '/appointments', icon: CalendarClock },
  { name: 'Doctors', to: '/doctors', icon: Stethoscope },
  { name: 'Beds', to: '/beds', icon: BedDouble },
  { name: 'Billing', to: '/billing', icon: CircleDollarSign },
];

export default function Sidebar() {
  return (
    <aside className="w-full bg-slate-950 p-6 text-white xl:w-72 xl:shrink-0">
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
        {sidebarItems.map(({ name, to, icon: Icon }) => (
          <NavLink
            key={name}
            to={to}
            end={to === '/'}
            className={({ isActive }) =>
              `flex w-full items-center justify-between rounded-2xl px-3 py-3 text-left text-sm transition ${
                isActive ? 'bg-cyan-500/20 text-cyan-200' : 'text-slate-300 hover:bg-slate-800'
              }`
            }
          >
            {({ isActive }) => (
              <>
                <span className="flex items-center gap-3">
                  <Icon className="h-4 w-4" />
                  {name}
                </span>
                {isActive ? <Sparkles className="h-4 w-4" /> : null}
              </>
            )}
          </NavLink>
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
  );
}
