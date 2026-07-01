import {

    useEffect,

    useState

} from "react"

import { api } from "../api"
import { useNavigate } from "react-router-dom"
import type { Incident } from "../types";
import {

    Table,

    TableHeader,

    TableBody,

    TableRow,

    TableCell,

    TableHead

} from "@/components/ui/table"

import SeverityBadge from "./SeverityBadge"

import StatusBadge from "./StatusBadge"

export default function IncidentTable() {

    const navigate = useNavigate()

    const [incidents, setIncidents] =

        useState<Incident[]>([])

    useEffect(() => {

        api

            .get("/incidents")

            .then(r => setIncidents(r.data))

    }, [])

    return (

        <Table>

            <TableHeader>

                <TableRow>

                    <TableHead>ID</TableHead>

                    <TableHead>Service</TableHead>

                    <TableHead>Severity</TableHead>

                    <TableHead>Status</TableHead>

                </TableRow>

            </TableHeader>

            <TableBody>

                {

                    incidents.map(i => (

                        <TableRow
                        key={i.incident_id}
                        className="cursor-pointer hover:bg-muted"
                        onClick={() =>
                            navigate(`/incidents/${i.incident_id}`)
                        }
                    >

                            <TableCell>

                                {i.incident_id}

                            </TableCell>

                            <TableCell>

                                {i.service_name}

                            </TableCell>

                            <TableCell>

                                <SeverityBadge

                                    severity={i.severity}

                                />

                            </TableCell>

                            <TableCell>

                                <StatusBadge

                                    status={i.status}

                                />

                            </TableCell>

                        </TableRow>

                    ))

                }

            </TableBody>

        </Table>

    )

}