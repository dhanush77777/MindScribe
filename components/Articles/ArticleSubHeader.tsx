"use client";

import { Plus } from "lucide-react";
import { Button } from "../ui/button";

function ArticleSubHeader() {
  return (
    <div className="flex items-center h-[60px] sticky top-0 left-0 bg-white z-10">
      <Plus className="w-6 h-6 text-[#6B6B6B] cursor-pointer hover:bg-[#6B6B6B]/10 rounded-full" />
      <Button variant="default" className="text-[#6B6B6B] underline decoration-black underline-offset-[23px]">
        For you
      </Button>
      <Button variant="default" className="text-[#6B6B6B]">
        Following
      </Button>
    </div>
  );
}

export default ArticleSubHeader;
