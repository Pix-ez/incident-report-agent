import { Badge } from "@/components/ui/badge"

interface Props{

    severity:string
}

export default function SeverityBadge({

    severity

}:Props){

    let variant:any="secondary"

    if(

        severity.toLowerCase()==="critical"

    )

        variant="destructive"

    return(

        <Badge variant={variant}>

            {severity}

        </Badge>

    )
}