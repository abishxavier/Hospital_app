import React from 'react';
import { 
  Users, 
  Activity, 
  Calendar, 
  DollarSign, 
  TrendingUp, 
  TrendingDown,
  Clock,
  UserPlus
} from 'lucide-react';
import { 
  AreaChart, 
  Area, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer,
  BarChart,
  Bar,
  Legend
} from 'recharts';

const patientData = [
  { name: 'Mon', patients: 120, opd: 80, ipd: 40 },
  { name: 'Tue', patients: 145, opd: 95, ipd: 50 },
  { name: 'Wed', patients: 130, opd: 85, ipd: 45 },
  { name: 'Thu', patients: 165, opd: 110, ipd: 55 },
  { name: 'Fri', patients: 180, opd: 120, ipd: 60 },
  { name: 'Sat', patients: 90, opd: 60, ipd: 30 },
  { name: 'Sun', patients: 70, opd: 45, ipd: 25 },
];

const revenueData = [
  { name: 'Jan', revenue: 4000 },
  { name: 'Feb', revenue: 3000 },
  { name: 'Mar', revenue: 2000 },
  { name: 'Apr', revenue: 2780 },
  { name: 'May', revenue: 1890 },
  { name: 'Jun', revenue: 2390 },
  { name: 'Jul', revenue: 3490 },
];

const StatCard = ({ title, value, icon: Icon, trend, trendValue, colorClass, bgClass }) => (
  <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-100 hover:shadow-md transition-shadow relative overflow-hidden group">
    <div className={`absolute -right-6 -top-6 w-24 h-24 rounded-full opacity-10 transition-transform group-hover:scale-110 ${bgClass}`}></div>
    
    <div className="flex justify-between items-start mb-4 relative z-10">
      <div>
        <p className="text-sm font-medium text-slate-500 mb-1">{title}</p>
        <h3 className="text-3xl font-bold text-slate-800">{value}</h3>
      </div>
      <div className={`p-3 rounded-xl ${bgClass} bg-opacity-10 backdrop-blur-sm`}>
        <Icon className={`w-6 h-6 ${colorClass}`} />
      </div>
    </div>
    
    <div className="flex items-center text-sm relative z-10">
      {trend === 'up' ? (
        <TrendingUp className="w-4 h-4 text-emerald-500 mr-1" />
      ) : (
        <TrendingDown className="w-4 h-4 text-rose-500 mr-1" />
      )}
      <span className={trend === 'up' ? 'text-emerald-500 font-medium' : 'text-rose-500 font-medium'}>
        {trendValue}
      </span>
      <span className="text-slate-400 ml-2">vs last month</span>
    </div>
  </div>
);

export default function AdminDashboard() {
  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-900 tracking-tight">Hospital Overview</h1>
          <p className="text-slate-500 mt-1">Welcome back, Admin. Here is what's happening today.</p>
        </div>
        <div className="flex space-x-3">
          <button className="px-4 py-2 bg-white border border-slate-200 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-50 transition-colors shadow-sm">
            Export Report
          </button>
          <button className="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 transition-colors shadow-sm shadow-blue-200">
            + New Staff
          </button>
        </div>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
        <StatCard 
          title="Total Patients" 
          value="1,248" 
          icon={Users} 
          trend="up" 
          trendValue="+12%"
          colorClass="text-blue-600"
          bgClass="bg-blue-500"
        />
        <StatCard 
          title="Avg. Occupancy" 
          value="84%" 
          icon={Activity} 
          trend="up" 
          trendValue="+5%"
          colorClass="text-indigo-600"
          bgClass="bg-indigo-500"
        />
        <StatCard 
          title="Appointments" 
          value="342" 
          icon={Calendar} 
          trend="down" 
          trendValue="-2%"
          colorClass="text-rose-600"
          bgClass="bg-rose-500"
        />
        <StatCard 
          title="Total Revenue" 
          value="$45,210" 
          icon={DollarSign} 
          trend="up" 
          trendValue="+18%"
          colorClass="text-emerald-600"
          bgClass="bg-emerald-500"
        />
      </div>

      {/* Charts Section */}
      <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
        {/* Main Chart */}
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 xl:col-span-2">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-lg font-bold text-slate-800">Patient Flow (OPD vs IPD)</h2>
            <select className="bg-slate-50 border border-slate-200 text-slate-700 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2">
              <option>This Week</option>
              <option>Last Week</option>
              <option>This Month</option>
            </select>
          </div>
          <div className="h-[300px] w-full">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={patientData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <defs>
                  <linearGradient id="colorOpd" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                  </linearGradient>
                  <linearGradient id="colorIpd" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#8b5cf6" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#8b5cf6" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />
                <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{fill: '#64748b', fontSize: 12}} dy={10} />
                <YAxis axisLine={false} tickLine={false} tick={{fill: '#64748b', fontSize: 12}} />
                <Tooltip 
                  contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }}
                />
                <Legend verticalAlign="top" height={36}/>
                <Area type="monotone" dataKey="opd" stroke="#3b82f6" strokeWidth={3} fillOpacity={1} fill="url(#colorOpd)" name="Outpatient (OPD)" />
                <Area type="monotone" dataKey="ipd" stroke="#8b5cf6" strokeWidth={3} fillOpacity={1} fill="url(#colorIpd)" name="Inpatient (IPD)" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Secondary Chart / List */}
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex flex-col">
          <h2 className="text-lg font-bold text-slate-800 mb-6">Recent Activity</h2>
          
          <div className="flex-1 space-y-6 overflow-y-auto pr-2">
            
            <div className="flex items-start">
              <div className="bg-blue-100 p-2 rounded-full mr-4 mt-1">
                <UserPlus className="w-4 h-4 text-blue-600" />
              </div>
              <div>
                <p className="text-sm font-semibold text-slate-800">New patient registered</p>
                <p className="text-xs text-slate-500 mt-1">John Doe • Cardiology</p>
                <p className="text-xs text-slate-400 mt-1 flex items-center"><Clock className="w-3 h-3 mr-1"/> 10 mins ago</p>
              </div>
            </div>

            <div className="flex items-start">
              <div className="bg-emerald-100 p-2 rounded-full mr-4 mt-1">
                <Activity className="w-4 h-4 text-emerald-600" />
              </div>
              <div>
                <p className="text-sm font-semibold text-slate-800">Surgery completed</p>
                <p className="text-xs text-slate-500 mt-1">Dr. Smith • OT Room 2</p>
                <p className="text-xs text-slate-400 mt-1 flex items-center"><Clock className="w-3 h-3 mr-1"/> 45 mins ago</p>
              </div>
            </div>

            <div className="flex items-start">
              <div className="bg-rose-100 p-2 rounded-full mr-4 mt-1">
                <Calendar className="w-4 h-4 text-rose-600" />
              </div>
              <div>
                <p className="text-sm font-semibold text-slate-800">Appointment cancelled</p>
                <p className="text-xs text-slate-500 mt-1">Sarah Connor • Neurology</p>
                <p className="text-xs text-slate-400 mt-1 flex items-center"><Clock className="w-3 h-3 mr-1"/> 1 hour ago</p>
              </div>
            </div>

             <div className="flex items-start">
              <div className="bg-indigo-100 p-2 rounded-full mr-4 mt-1">
                <Users className="w-4 h-4 text-indigo-600" />
              </div>
              <div>
                <p className="text-sm font-semibold text-slate-800">Shift Change</p>
                <p className="text-xs text-slate-500 mt-1">Nursing Staff • ICU Ward</p>
                <p className="text-xs text-slate-400 mt-1 flex items-center"><Clock className="w-3 h-3 mr-1"/> 2 hours ago</p>
              </div>
            </div>
            
          </div>
          
          <button className="mt-4 w-full py-2 text-sm font-medium text-blue-600 bg-blue-50 hover:bg-blue-100 rounded-lg transition-colors">
            View All Activity
          </button>
        </div>
      </div>
    </div>
  );
}
