import { useRouter } from "next/navigation";
import Link from "next/link";

export default function Error() {
  const router = useRouter();
  const { query } = router || {}; // Check if router exists before destructuring
  const { status, statusText } = query || {}; // Check if query exists before destructuring

  return (
    <div className="m-5">
      <h1 className="text-xl">Error</h1>
      <p className="text-xs mb-2">Something went wrong.</p>
      <p className="mb-3">
        <code>
          {status}: {statusText}
        </code>
      </p>
      <Link href="/">🔙 take me home</Link>
      <footer className="mt-4 text-xs"></footer>
    </div>
  );
}
