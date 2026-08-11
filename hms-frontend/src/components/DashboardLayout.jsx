import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';

export default function DashboardLayout() {
  return (
    <div className="min-h-screen bg-[radial-gradient(circle_at_top_left,_rgba(56,189,248,0.18),_transparent_35%),linear-gradient(135deg,_#f8fbff_0%,_#eef4ff_100%)] p-4 text-slate-800 lg:p-6">
      <div className="mx-auto flex min-h-[calc(100vh-2rem)] max-w-7xl flex-col overflow-hidden rounded-[32px] border border-white/70 bg-white/80 shadow-[0_30px_90px_rgba(15,23,42,0.14)] backdrop-blur xl:flex-row">
        <Sidebar />
        <main className="flex-1 bg-slate-50/80 p-4 lg:p-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
