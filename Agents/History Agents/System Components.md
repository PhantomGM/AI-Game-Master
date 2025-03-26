## 1. System Components

### 1.1 Core AI Personalities
Each personality maintains state tracking their previous contributions and focus areas.

#### 1.1.1 Idealist Visionary
- Primary Focus: Progress, transformation, unity
- Table Preferences: Good Table, Personal Table (Achievements, Values)
- Tone Tendency: Light
- Creation Style: Focuses on breakthroughs and achievements

#### 1.1.2 Pragmatic Realist
- Primary Focus: Economics, resources, power dynamics
- Table Preferences: Economic, Military tables
- Tone Tendency: Mixed
- Creation Style: Emphasizes practical consequences

#### 1.1.3 Cultural Anthropologist
- Primary Focus: Societies, traditions, beliefs
- Table Preferences: [[Culture]], Religious tables
- Tone Tendency: Mixed
- Creation Style: Explores cultural patterns

#### 1.1.4 Conflict Theorist
- Primary Focus: Struggles, tensions, power shifts
- Table Preferences: Bad Table, Political table
- Tone Tendency: Dark
- Creation Style: Highlights conflicts and changes

### 1.2 Input Processing

#### 1.2.1 World State Analysis
- Input: Current [[World]] state document
- Process: Analyzes key features, relationships, and conditions
- Output: Structured data for [[History]] generation

#### 1.2.2 Existing Palette Processing
- Input: [[World]]-provided palette (if any)
- Process: Extracts constraints and requirements
- Output: Initial YES/NO lists for modification

### 1.3 History Generation Components

#### 1.3.1 Big Picture Generator
- Input: [[World]] state analysis
- Process: Distills core narrative thread
- Output: Single sentence describing historical arc

#### 1.3.2 Bookend Creator
- Input: [[World]] state, [[Big Picture]]
- Process: Establishes starting conditions
- Output: [[Starting Period]] description

## 2. Operational Flow

### 2.1 Initialization Phase

```plaintext
1. Load World State
   ├── Process world document
   ├── Extract key parameters
   └── Generate structured world data

2. Generate Big Picture
   ├── Analyze world transformation
   ├── Identify key elements
   └── Create concise narrative sentence

3. Create Starting Period
   ├── Establish initial conditions
   ├── Define baseline parameters
   └── Document starting point

4. Palette Creation
   ├── IF world palette exists:
   │   ├── Load existing constraints
   │   └── Each personality adds elements
   └── IF no world palette:
       ├── Personalities create from scratch
       └── Continue until pass received
```

### 2.2 History Generation Phase

```plaintext
1. First Pass
   ├── Each personality creates initial element
   └── Elements placed in timeline

2. Focus Rounds
   ├── Select Lens (random personality)
   ├── Lens declares Focus
   ├── Creation sequence:
   │   ├── Lens creates (can make two nested items)
   │   ├── Second personality creates
   │   ├── Third personality creates
   │   ├── Fourth personality creates
   │   └── Lens final creation
   ├── Legacy selection
   └── Legacy exploration
```

### 2.3 Period Creation Rules

```plaintext
1. Period Emergence Conditions
   ├── Significant world state change
   ├── Distinct historical phase
   ├── New dominant forces
   └── Gap in historical progression

2. Period Creation Decision Tree
   ├── IF major shift detected:
   │   └── Create new period
   ├── IF minor development:
   │   └── Add event to existing period
   └── IF elaboration needed:
       └── Create scene within event
```

## 3. Supporting Systems

### 3.1 Inspiration Tables
- Standard Tables: Economic, Military, Political, Religious, Social
- Specialized Tables: Nature, [[Culture]], Good/Bad, Personal
- Table Selection: Based on personality and focus

### 3.2 Oracle System
- Purpose: Yes/No decision support
- Input: Question with probability
- Output: Binary decision with justification

### 3.3 Tone System
- Light/Dark determination
- Personality influence on tone
- Historical context consideration

## 4. Output Generation

### 4.1 History Documentation
- Chronological timeline
- Period descriptions
- Event details
- Scene records

### 4.2 Relationship Tracking
- Inter-period connections
- Event chains
- Legacy impacts
- Cultural developments

## 5. System Controls

### 5.1 Consistency Checks
- Timeline coherence
- Palette compliance
- Historical logic
- Character continuity

### 5.2 Balance Mechanisms
- Period distribution
- Tone variation
- Focus diversity
- Personality contribution tracking