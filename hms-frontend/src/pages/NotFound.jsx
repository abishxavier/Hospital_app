import { Link } from 'react-router-dom';

export default function NotFound() {
  return (
    <div className="flex h-full min-h-[60vh] flex-col items-center justify-center rounded-[28px] border border-slate-200 bg-white p-10 text-center shadow-sm">
      <p className="text-sm uppercase tracking-[0.3em] text-cyan-600">404</p>
      <h1 className="mt-2 text-2xl font-semibold text-slate-900">Page not found</h1>
      <p className="mt-2 text-sm text-slate-500">The page you're looking for doesn't exist.</p>
      <Link to="/" className="mt-5 rounded-full bg-slate-900 px-4 py-2 text-sm font-medium text-white">
        Back to overview
      </Link>
    </div>
  );
}
