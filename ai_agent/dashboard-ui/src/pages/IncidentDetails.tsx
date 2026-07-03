import  { api } from "../api"
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"


import { useNavigate } from "react-router-dom"

import IncidentInfoCard from "../components/IncidentInfoCard"
import AnalysisCard from "../components/AnalysisCard"
import RecommendationCard from "../components/RecommendationCard"
import InvestigationTabs from "../components/InvestigationTabs"

import { Button } from "@/components/ui/button"
import {
    ArrowLeft,
    Check,
    X,
    ShieldCheck
} from "lucide-react"
import type { Incident } from "@/types"


export default function IncidentDetails() {


    const navigate = useNavigate()
    const { incidentId } = useParams()
    const [loading, setLoading] = useState(true)

    const [incident, setIncident] = useState<Incident>()

    const [analysis, setAnalysis] = useState<any>()

    const [investigation, setInvestigation] = useState()

    useEffect(() => {

        async function load() {

            setLoading(true)
            try {
                
                const incidentRes =
                    await api.get(`/incidents/${incidentId}`)
                    setIncident(incidentRes.data)
            } catch (error) {
                console.log(error)                
            }
            try {
                
                const analysisRes =await api.get(`/analysis/${incidentId}`)
                setAnalysis(analysisRes.data)
            } catch (error) {
                console.log(error)                
            }
            try {
                const investigationRes =await api.get(`/investigations/${incidentId}`)

                setInvestigation(
                    investigationRes.data
                )

            } catch (error) {
                console.log(error)                
            }
            finally{
                setLoading(false)
            }

            
        }

        load()

    }, [incidentId])
    
    if (loading) {

        return <div>loading</div>

    }

    if (!incident) {

        return <div>Incident not found.</div>

    }

    if (!analysis) {

        return <div>No AI analysis available yet.</div>

    }

    if (!investigation) {

        return <div>No investigation available.</div>

    }

    return (

        <div className="min-h-screen bg-muted/30">

            <div className="max-w-7xl mx-auto p-8">

                {/* Header */}

                <div className="flex items-center justify-between mb-8">

                    <div>

                        <Button
                            variant="ghost"
                            onClick={() => navigate("/")}
                        >

                            <ArrowLeft className="mr-2 h-4 w-4"/>

                            Back

                        </Button>

                        <h1 className="text-3xl font-bold mt-3">

                            Incident {incident.incident_id}

                        </h1>

                    </div>

                </div>


                {/* Top Grid */}

                <div className="grid grid-cols-2 gap-6">

                    <IncidentInfoCard
                        incident={incident}
                    />

                    <AnalysisCard
                        analysis={analysis}
                    />

                </div>


                {/* Recommendations */}

                <div className="mt-6">

                    <RecommendationCard
                        recommendations={
                            analysis.recommendations
                        }
                    />

                </div>


                {/* Investigation */}

                <div className="mt-6">

                    <InvestigationTabs
                        investigation={investigation}
                    />

                </div>


                {/* Human Review */}

                <div className="mt-8">

                    <div className="border rounded-xl bg-background p-6">

                        <h2 className="text-xl font-semibold mb-5">

                            Human Review

                        </h2>

                        <div className="flex gap-4">

                            <Button>

                                <Check className="mr-2 h-4 w-4"/>

                                Approve AI

                            </Button>

                            <Button
                                variant="destructive"
                            >

                                <X className="mr-2 h-4 w-4"/>

                                Reject

                            </Button>

                            <Button
                                variant="secondary"
                            >

                                <ShieldCheck className="mr-2 h-4 w-4"/>

                                Resolve Incident

                            </Button>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    )

}