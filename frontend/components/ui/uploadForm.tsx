import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export default function UploadForm() {
  return (
    <div className="absolute bottom-25 grid w-full max-w-sm items-center gap-1.5">
      <Label htmlFor="picture">Picture</Label>
      <Input id="picture" type="file" />
    </div>
  );
}
