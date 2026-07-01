import {
    Card,
    CardContent,
    CardHeader,
    CardTitle
} from "@/components/ui/card"

import { CheckCircle2 } from "lucide-react"

interface Props {

    recommendations: string[]

}

export default function RecommendationCard({

    recommendations

}: Props) {

    return (

        <Card>

            <CardHeader>

                <CardTitle>

                    AI Recommendations

                </CardTitle>

            </CardHeader>

            <CardContent>

                <div className="space-y-4">

                    {

                        recommendations.map(

                            (

                                recommendation,

                                index

                            ) => (

                                <div
                                    key={index}
                                    className="flex gap-3"
                                >

                                    <CheckCircle2
                                        className="text-green-600 mt-1"
                                        size={18}
                                    />

                                    <span>

                                        {recommendation}

                                    </span>

                                </div>

                            )

                        )

                    }

                </div>

            </CardContent>

        </Card>

    )

}