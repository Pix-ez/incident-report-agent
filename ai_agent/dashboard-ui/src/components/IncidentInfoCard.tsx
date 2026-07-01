import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import SeverityBadge from "./SeverityBadge"
import StatusBadge from "./StatusBadge"

interface Props {
    incident: any
}

export default function IncidentInfoCard({ incident }: Props) {

    const Row = ({ label, value }: any) => (
        <div className="flex justify-between py-2 border-b last:border-none">
            <span className="text-muted-foreground">{label}</span>
            <span className="font-medium">{value}</span>
        </div>
    )

    return (

        <Card>

            <CardHeader>

                <CardTitle>

                    Incident Information

                </CardTitle>

            </CardHeader>

            <CardContent className="space-y-2">

                <Row
                    label="Incident ID"
                    value={incident.incident_id}
                />

                <Row
                    label="Service"
                    value={incident.service_name}
                />

                <div className="flex justify-between py-2">

                    <span className="text-muted-foreground">

                        Severity

                    </span>

                    <SeverityBadge
                        severity={incident.severity}
                    />

                </div>

                <div className="flex justify-between py-2">

                    <span className="text-muted-foreground">

                        Status

                    </span>

                    <StatusBadge
                        status={incident.status}
                    />

                </div>

                <Row
                    label="Alert"
                    value={incident.alert_name}
                />

                <Row
                    label="Created"
                    value={
                        new Date(
                            incident.created_at
                        ).toLocaleString()
                    }
                />

            </CardContent>

        </Card>

    )

}