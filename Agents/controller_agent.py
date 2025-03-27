import openai
import os

from Primary_Agents.memory_keeper_agent import MemoryKeeperAgent

class ControllerAgent:
    def __init__(self):
        # Initialize agents and other necessary components
        self.agents = {}  # Dictionary to store agent instances
        self.game_state = {}  # Dictionary to store game state information
        # Initialize LLM API client
        self.openai_client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        # Initialize the MemoryKeeperAgent and store it in the agents dictionary
        self.agents["Memory Keeper"] = MemoryKeeperAgent() 
        self.system_prompt = """You are the Controller Agent, the central coordinator of a Multi-Agent AI Game Master system. Your primary function is to process player inputs, determine which specialized agents to consult, gather their responses, and synthesize them into coherent, engaging game narration.

PRIMARY RESPONSIBILITIES:
1. Receive and classify player inputs (actions, questions, dialogue, etc.)
2. Determine which specialized agents to consult based on input type
3. Formulate specific queries for each relevant specialized agent
4. Synthesize agent responses into unified, natural game narration
5. Maintain conversation flow and overall game state
6. Track active storylines, immediate context, and current scene parameters

OPERATIONAL GUIDELINES:
- Prioritize responsiveness - aim for low-latency interactions
- Maintain consistent narrative voice and tone throughout sessions
- Highlight significant game events, dramatic moments, and key decisions
- Balance detail with pacing - elaborate on important elements, summarize routine ones
- Present choices and consequences clearly to players
- Recognize and adapt to shifts in player engagement or interest

INTERACTION PROTOCOLS:
- When receiving player input, identify the primary intention (action, question, roleplay, etc.)
- Formulate specific queries for each required specialized agent using standardized formats
- Integrate responses from multiple agents, resolving conflicts where necessary
- Present results in a narrative format appropriate to the game context
- When facing ambiguous player input, ask clarifying questions
- Maintain a consistent tone aligned with the established campaign style

AGENT INTEGRATION:
- Rules Reference: Query for mechanical rulings and consequences
- Memory Keeper: Request relevant past events and established facts
- NPC Manager: Request dialogue and reactions for non-player characters
- World Builder: Request environmental details and location information
- Narrative Designer: Request plot developments and story implications
- Combat Choreographer: Request detailed combat narration
- Session Manager: Consult on pacing and session structure
- Rule of Cool: Consult on potential extraordinary moment opportunities

INPUT PROCESSING FRAMEWORK:
For standard gameplay, process input through this framework:
1. What is the player attempting to do?
2. Which game mechanics are relevant to this action?
3. What established facts or history are relevant?
4. How does this action impact the narrative?
5. What sensory details would enhance this moment?
6. Which NPCs are involved or affected?
7. Is this a potential Rule of Cool moment?

OUTPUT STRUCTURE:
Structure your responses to include as appropriate:
1. Narrative description with sensory details
2. NPC dialogue or reactions
3. Mechanical results or consequences
4. Player options or choices
5. Relevant rule clarifications when necessary

You are the voice of the Game Master that players interact with directly. Maintain an engaging, responsive, and adaptive presence while seamlessly integrating the specialized knowledge and capabilities of the entire agent network."""

    def _llm_call(self, prompt, model="gpt-3.5-turbo", **kwargs):  # You can adjust the model as needed
        """Makes a call to the LLM API with the given prompt."""
        try:
            messages = [{"role": "system", "content": self.system_prompt}, {"role": "user", "content": prompt}]
            response = self.openai_client.chat.completions.create(
                model=model,
                messages=messages,
                **kwargs,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error during LLM API call: {e}")
            return None
    def call_agent(self, agent_name, player_input, game_context):
        """Simulates calling an agent and getting a response.  Placeholder for now."""
        if agent_name == "Memory Keeper":
            # Call the appropriate MemoryKeeperAgent tool based on the context or input
            # (We'll need to refine this logic later to determine which tool to call)
            print(f"Calling Memory Keeper with input: {player_input} and context: {game_context}")
            # For now, just call the record_event tool as a placeholder
            response = self.agents["Memory Keeper"].record_event(
                event_type="placeholder", 
                description="Placeholder event", 
                details={"input": player_input, "context": game_context}
            )
            return response

    def process_player_input(self, player_input):
        """Processes player input and initiates the appropriate actions."""
        # Use an LLM to understand player intent
        intent_prompt = f"Determine the intent of the following player input: '{player_input}'. Provide the intent as a single phrase."
        intent = self._llm_call(intent_prompt)

        # Extract relevant information (e.g., entities, actions)
        details_prompt = f"Extract key details (actions, objects, characters, etc.) from the following player input: '{player_input}'. Provide the details as a comma-separated list."
        details = self._llm_call(details_prompt)
        
        # Detect player-to-player communication
        communication_prompt = f"Is the following input likely communication between players (in or out of character), rather than an action directed at the game world or an NPC? Answer 'yes' or 'no'. Input: '{player_input}'"
        is_player_communication = self._llm_call(communication_prompt)
        player_communication = is_player_communication.lower() == "yes" if is_player_communication else False

        player_input_data = {"intent": intent, "details": details}        

        # Get the current game context
        game_context = self.get_game_context()
        # Update the game context with the player_communication flag
        game_context["player_communication"] = player_communication

        # Determine which agents to call        
        if not player_communication:
            agents_to_call = self.agent_routing_decision_tree(player_input_data, game_context)
        else:
            agents_to_call = []

        # Ensure Memory Keeper is always called
        if "Memory Keeper" not in agents_to_call:
            agents_to_call.append("Memory Keeper")

        agent_responses = {}
        for agent_name in agents_to_call:
            agent_responses[agent_name] = self.call_agent(agent_name, player_input_data, game_context)
        if not player_communication:
           final_response = self.synthesize_responses(agent_responses)

        return final_response    

        # Ensure Memory Keeper is always called
        if "Memory Keeper" not in agents_to_call:
            agents_to_call.append("Memory Keeper")

    def get_game_context(self):
        """Retrieves the current game context.  Placeholder for now."""
        # In a real system, this would access game state, recent events, etc.
        return {
            "scene": "exploration",
            "location": "Forest",
            "active_quest": "Find the hidden temple",
            "characters_involved": [],
            "recent_events": [],
            "turn": "player",
            "skill_check_in_progress": None,
            "target_npc": None,
            "combat_state": None,
            "conversation_history": [],
            "direct_question_topic": None,
            "player_communication": False,
        }

    def response_priority_manager(self, agent_responses):
        """Manages the priority of responses from different agents."""
        # Implementation: Logic to prioritize responses based on relevance or importance.
        pass

    def context_window_manager(self, conversation_history):
        """Manages the context window for interactions with agents and the player."""
        # Implementation: Maintain a history of recent interactions and manage its size.
        pass

    def modal_operation_coordinator(self, mode):
        """Coordinates operations in different modes (e.g., history creation)."""
        # Implementation: Logic to switch between different game modes and manage their specific processes.
        pass

    def game_state_persistence_manager(self, action="save" or "load"):
        """Manages loading and saving the game state."""
        # Implementation: Use a database or file system to persist game state data.
        pass

    def maintain_conversation_flow(self, player_input, output):
        """Manages the flow of conversation and ensures a natural interaction."""
        # Implementation: Use techniques to track conversation turns, manage topic changes,
        # and ensure responses are contextually appropriate.
        pass
    

    def update_game_state(self, updates):
        """Updates the game state with new information."""
        # Implementation: Modify the self.game_state dictionary based on agent responses
        # or player actions.
        pass
