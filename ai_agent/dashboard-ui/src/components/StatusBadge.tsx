import { Badge } from "@/components/ui/badge"

interface Props{

    status:string
}

export default function StatusBadge({

    status

}:Props){

    let variant:any="secondary"

    if(status==="WAITING_HUMAN")

        variant="destructive"

    if(status==="RESOLVED")

        variant="default"

    return(

        <Badge variant={variant}>

            {status}

        </Badge>

    )
}