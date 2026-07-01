import Sidebar from "../components/Sidebar"

import IncidentTable from "../components/IncidentTable"

import { Card } from "@/components/ui/card"

export default function Dashboard(){

return(

<div className="flex">

<Sidebar/>

<div className="flex-1 p-8">

<h1

className="text-3xl font-bold mb-6"

>

AI Incident Response Dashboard

</h1>

<Card className="p-6">

<IncidentTable/>

</Card>

</div>

</div>

)

}