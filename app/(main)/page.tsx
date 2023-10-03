import ArticleFeed from "./(feed)/ArticleFeed";
import SideBarFeed from "./(feed)/SideBarFeed";

export default function Home() {
  return (
    <main className="w-full grid grid-cols-3 max-w-6xl mx-auto">
      <div className="col-span-3 md:col-span-2 mt-1 p-5">
        <ArticleFeed />
      </div>
      <div className="hidden md:flex col-span-1">
        <SideBarFeed />
      </div>
    </main>
  );
}
