import {

    Tabs,

    TabsContent,

    TabsList,

    TabsTrigger

} from "@/components/ui/tabs"

import JsonViewer from "./JsonViewer"

interface Props {

    investigation: any

}

export default function InvestigationTabs({

    investigation

}: Props) {

    return (

        <Tabs defaultValue="metrics">

            <TabsList>

                <TabsTrigger value="metrics">

                    Metrics

                </TabsTrigger>

                <TabsTrigger value="logs">

                    Logs

                </TabsTrigger>

                <TabsTrigger value="history">

                    History

                </TabsTrigger>

            </TabsList>

            <TabsContent value="metrics">

                <JsonViewer
                    title="Prometheus Metrics"
                    data={investigation.metrics_data}
                />

            </TabsContent>

            <TabsContent value="logs">

                <JsonViewer
                    title="Loki Logs"
                    data={investigation.logs_data}
                />

            </TabsContent>

            <TabsContent value="history">

                <JsonViewer
                    title="Historical Incidents"
                    data={
                        investigation.historical_events
                    }
                />

            </TabsContent>

        </Tabs>

    )

}