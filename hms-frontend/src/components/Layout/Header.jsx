import React from 'react';
import { Bell, UserCircle } from 'lucide-react';

export default function Header() {
  return (
    <header className="h-16 bg-white border-b border-slate-200 flex items-center justify-between px-6">
      <div className="flex-1"></div>
      
      <div className="flex items-center space-x-4">
        <button className="text-slate-500 hover:text-slate-700 relative">
          <Bell className="w-6 h-6" />
          <span className="absolute top-0 right-0 w-2 h-2 bg-red-500 rounded-full"></span>
        </button>
        
        <div className="flex items-center space-x-2 border-l pl-4 border-slate-200 cursor-pointer">
          <UserCircle className="w-8 h-8 text-slate-600" />
          <div className="text-sm">
            <p className="font-medium text-slate-900">Dr. Sarah Johnson</p>
            <p className="text-slate-500 text-xs">Cardiology</p>
          </div>
        </div>
      </div>
    </header>
  );
}
