import {

    ShieldAlert,

    LayoutDashboard

} from "lucide-react"

export default function Sidebar() {

    return (

        <div className="w-64 border-r bg-muted/30 h-screen">

            <div className="p-6">

                <h1 className="font-bold text-xl">

                    Incident AI

                </h1>

            </div>

            <div className="space-y-2 p-4">

                <div className="flex gap-2 items-center">

                    <LayoutDashboard size={18}/>

                    Dashboard

                </div>

                <div className="flex gap-2 items-center">

                    <ShieldAlert size={18}/>

                    Incidents

                </div>

            </div>

        </div>
    )
}