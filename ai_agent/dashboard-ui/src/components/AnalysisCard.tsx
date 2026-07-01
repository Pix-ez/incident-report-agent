import {
    Card,
    CardContent,
    CardHeader,
    CardTitle
} from "@/components/ui/card"

interface Props {

    analysis: any

}

export default function AnalysisCard({

    analysis

}: Props) {

    return (

        <Card>

            <CardHeader>

                <CardTitle>

                    AI Root Cause Analysis

                </CardTitle>

            </CardHeader>

            <CardContent className="space-y-5">

                <div>

                    <p className="text-sm text-muted-foreground">

                        Root Cause

                    </p>

                    <p className="font-semibold mt-1">

                        {analysis.root_cause}

                    </p>

                </div>

                <div className="grid grid-cols-2 gap-4">

                    <div>

                        <p className="text-sm text-muted-foreground">

                            Confidence

                        </p>

                        <p className="text-xl font-bold">

                            {analysis.confidence}%

                        </p>

                    </div>

                    <div>

                        <p className="text-sm text-muted-foreground">

                            Severity

                        </p>

                        <p className="font-semibold">

                            {analysis.severity}

                        </p>

                    </div>

                </div>

            </CardContent>

        </Card>

    )

}