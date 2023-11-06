import { Nullable } from './utils'

export interface AgentWithConfigs {
  agent: {
    id: string
    name: string
    description: string
    role: string
    creator: Nullable<Creator>
    avatar: string
  }
  configs: {
    goals: string[]
    instructions: string[]
    constraints: string[]
    suggestions: string[]
    tools: string[]
    datasources: string[]
    greeting: string
    text: string
  }
  system_message: Nullable<string>
}

interface Creator {
  name: string
  avatar: string
}
