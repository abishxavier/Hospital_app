import { Search } from 'lucide-react';

export default function PageHeader({ eyebrow, title, subtitle, searchPlaceholder }) {
  return (
    <header className="rounded-[28px] bg-gradient-to-br from-slate-900 via-slate-800 to-cyan-700 p-6 text-white shadow-lg">
      <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
        <div>
          {eyebrow ? <p className="text-sm uppercase tracking-[0.3em] text-cyan-200">{eyebrow}</p> : null}
          <h1 className="mt-2 text-3xl font-semibold">{title}</h1>
          {subtitle ? <p className="mt-2 text-sm text-slate-300">{subtitle}</p> : null}
        </div>
        {searchPlaceholder ? (
          <div className="flex items-center gap-3 rounded-2xl border border-white/15 bg-white/10 px-4 py-3 backdrop-blur">
            <Search className="h-4 w-4 text-cyan-200" />
            <input className="w-40 bg-transparent text-sm outline-none placeholder:text-slate-300" placeholder={searchPlaceholder} />
          </div>
        ) : null}
      </div>
    </header>
  );
}
