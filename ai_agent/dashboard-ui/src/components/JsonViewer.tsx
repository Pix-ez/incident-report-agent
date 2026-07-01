import {
    Card,
    CardContent,
    CardHeader,
    CardTitle
} from "@/components/ui/card"

interface Props {

    title: string

    data: any

}

export default function JsonViewer({

    title,

    data

}: Props) {

    return (

        <Card>

            <CardHeader>

                <CardTitle>

                    {title}

                </CardTitle>

            </CardHeader>

            <CardContent>

                <pre className="overflow-auto rounded-md bg-muted p-4 text-xs">

                    {

                        JSON.stringify(

                            data,

                            null,

                            2

                        )

                    }

                </pre>

            </CardContent>

        </Card>

    )

}