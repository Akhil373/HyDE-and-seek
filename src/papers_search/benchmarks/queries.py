queries = [
    # --- LEVEL 1: Exact / Keyword Queries (Easy) ---
    ("SCOPE: Signal-Calibrated On-Policy Distillation Enhancement", "2604.10688"),
    ("BMdataset LilyPond symbolic music", "2604.10628"),
    ("EquiformerV3 SE(3)-equivariant graph attention", "2604.09130"),
    ("DiningBench multi-view food dataset", "2604.10425"),
    ("CodeTracer architecture for agent states", "2604.11641"),
    # --- LEVEL 2: Conversational / Problem-Solution Queries (Medium) ---
    (
        "My LLM agent keeps forgetting who it is and mimics the user over long chats. How do I fix this?",
        "2604.09212",
    ),  # SPASM
    (
        "I need a way to track data lineage and see where my post-training dataset came from.",
        "2604.10480",
    ),  # Tracing the Roots
    (
        "Are there any benchmarks that test if LLMs can actually predict real-world chemistry and biology experiments?",
        "2604.10718",
    ),  # SciPredict
    (
        "I want to speed up my diffusion model by replacing it with a smaller model during some of the denoising steps.",
        "2604.02340",
    ),  # Not All Denoising Steps Are Equal
    (
        "How can I compress my LLM to 2-bit precision using additive quantization and fix the initialization bottlenecks?",
        "2604.08118",
    ),  # Initialisation Determines the Basin
    (
        "I need to evaluate my digital agent on tasks that require vision, search, and coding all at once.",
        "2604.11201",
    ),  # CocoaBench
    # --- LEVEL 3: Vague / Conceptual Queries (Hard) ---
    (
        "Using video game physics engines to teach AI how to solve science Olympiad problems.",
        "2604.11805",
    ),  # Solving Physics Olympiad
    (
        "That paper about how vision-language models completely fail when you rotate or scale an image.",
        "2604.01848",
    ),  # Semantic Richness or Geometric Reasoning
    (
        "Using an attacker-defender setup to teach language models how to manipulate beliefs and understand theory of mind.",
        "2604.11666",
    ),  # Playing Along
    (
        "A framework for software engineering agents that uses a sliding window to compress history so it doesn't forget the context.",
        "2604.11716",
    ),  # SWE-AGILE
    (
        "How human babies learn about the physical world so efficiently compared to AI.",
        "2604.10333",
    ),  # Zero-shot World Models
    (
        "Hacking distributed pipeline training by injecting a trigger word.",
        "2604.02372",
    ),  # Backdoor Attacks on Decentralised Post-Training
    # --- LEVEL 4: Highly Specific Niche & Cross-Disciplinary (Stress Tests) ---
    (
        "Applying Peircean semiotic theory to evaluate human-AI interaction in generative art.",
        "2604.08641",
    ),  # SemJudge
    (
        "Addressing the issue where transformers focus too much on specific, uninformative tokens.",
        "2604.10098",
    ),  # Attention Sink in Transformers
    (
        "Generating text-to-audio-video and testing the gaps in musical pitch control.",
        "2604.08540",
    ),  # AVGen-Bench
    (
        "Improving prompt optimization by filtering out bad user prompts to reduce response variance.",
        "2604.08801",
    ),  # p1
    (
        "Synthesizing human-object interaction videos conditioned on text, audio, and poses.",
        "2604.11804",
    ),  # OmniShow
    (
        "Can diffusion models and decision trees be understood under the same mathematical framework?",
        "2605.00414",
    ),  # Trees to Flows and Back
    (
        "A method that turns hierarchical decision logic into neural networks through distillation.",
        "2605.00414",
    ),  # Trees to Flows and Back
    (
        "Bridging discrete branching models and continuous generative processes with a shared optimization principle.",
        "2605.00414",
    ),  # Trees to Flows and Back
    (
        "Multi-agent system for extracting structured information from large-scale web searches.",
        "2604.27221",
    ),  # Web2BigTable
    (
        "How can multiple AI agents coordinate to build large tables from heterogeneous internet sources?",
        "2604.27221",
    ),  # Web2BigTable
    (
        "A framework where search workers share discoveries and iteratively improve decomposition strategies over time.",
        "2604.27221",
    ),  # Web2BigTable
    (
        "Joint audio and video generation for talking head synthesis using diffusion models.",
        "2604.23586",
    ),  # Talker-T2AV
    (
        "Generating synchronized speech and facial motion with a unified autoregressive architecture.",
        "2604.23586",
    ),  # Talker-T2AV
    (
        "Separating semantic coordination from low-level rendering when producing talking avatars.",
        "2604.23586",
    ),  # Talker-T2AV
    (
        "Reducing hallucinations in vision-language models through online self-calibration.",
        "2605.00323",
    ),  # OSCAR
    (
        "Using Monte Carlo tree search to improve visual grounding in multimodal models.",
        "2605.00323",
    ),  # OSCAR
    (
        "A system that teaches a model to trust what it can verify instead of guessing unseen image details.",
        "2605.00323",
    ),  # OSCAR
    (
        "Distributed black-box optimization using language models to coordinate agents.",
        "2605.00691",
    ),  # LAC-MAS
    (
        "Learning cooperation strategies for decentralized consensus optimization.",
        "2605.00691",
    ),  # LAC-MAS
    (
        "Replacing handcrafted swarm coordination rules with trajectory-driven self-design.",
        "2605.00691",
    ),  # LAC-MAS
    (
        "Cross-script voice cloning while preserving speaker identity across Indic languages.",
        "2605.00777",
    ),  # LASE
    (
        "Language-adversarial speaker embeddings for multilingual text-to-speech systems.",
        "2605.00777",
    ),  # LASE
    (
        "Making voice representations ignore language and script while retaining who is speaking.",
        "2605.00777",
    ),  # LASE
    (
        "Structured representation of agent skills for discovery and risk assessment.",
        "2604.24026",
    ),  # SSL Representation
    (
        "How can AI agents represent reusable skills beyond plain text instructions?",
        "2604.24026",
    ),  # SSL Representation
    (
        "Breaking a capability into scheduling signals, execution structure, and action logic.",
        "2604.24026",
    ),  # SSL Representation
    (
        "Cross-modal retrieval between analog circuit schematics, netlists, and descriptions.",
        "2604.23195",
    ),  # AnalogRetriever
    (
        "Searching analog circuit designs across multiple representations.",
        "2604.23195",
    ),  # AnalogRetriever
    (
        "A shared embedding space that lets engineers retrieve hardware designs regardless of format.",
        "2604.23195",
    ),  # AnalogRetriever
    (
        "Fleet-scale reinforcement learning for continuously improving robot policies.",
        "2605.00416",
    ),  # Learning While Deploying
    (
        "Using deployed robot experience and human interventions to improve VLA models.",
        "2605.00416",
    ),  # Learning While Deploying
    (
        "A robotic learning system that keeps getting better after deployment through shared fleet experience.",
        "2605.00416",
    ),  # Learning While Deploying
    (
        "Multilingual code reward models that score code quality across multiple criteria.",
        "2605.00754",
    ),  # Themis
    (
        "Reward models for evaluating code beyond functional correctness.",
        "2605.00754",
    ),  # Themis
    (
        "Training AI judges that can critique software in different languages and along multiple dimensions.",
        "2605.00754",
    ),  # Themis
    (
        "Find me a benchmark that tests AI agents on real-world expert tasks like law and finance.",
        "2603.07980",
    ),  # OneMillion-Bench
    (
        "Is there a paper that does speech recognition by editing a transcript instead of generating it token by token?",
        "2603.08397",
    ),  # NLE
    (
        "Looking for research where an AI agent runs architecture search experiments completely on its own.",
        "2603.07300",
    ),  # AutoResearch-RL
    (
        "I saw a paper arguing that noisy diffusion steps don't need full image resolution. Anyone know it?",
        "2603.08709",
    ),  # Scale Space Diffusion
    (
        "Find me the work showing BitNet models are naturally compatible with N:M sparsity.",
        "2603.05168",
    ),  # Sparse-BitNet
    (
        "What's that benchmark with decades of treasury documents that current AI agents struggle on?",
        "2603.08655",
    ),  # OfficeQA Pro
    (
        "I'm looking for a benchmark that evaluates AI agents on scientific literature discovery.",
        "2604.25256",
    ),  # AutoResearchBench
    (
        "Find the study that compared text-to-speech systems across multiple Indian languages using human preferences.",
        "2604.21481",
    ),  # Preferences of a Voice-First Nation
    (
        "Is there an AI scientist specifically for computational fluid dynamics research?",
        "2605.06607",
    ),  # AI CFD Scientist
    (
        "Looking for a paper that distills knowledge between language models with different tokenizers.",
        "2604.07466",
    ),  # Byte-Level Distillation
    (
        "Can AI agents navigate legal statutes and regulations instead of stuffing the whole ruleset into context?",
        "2606.05009",
    ),  # DAR
    (
        "Find me a benchmark for evaluating scientific reasoning using procedurally generated repositories.",
        "2604.13201",
    ),  # InfiniteScienceGym
    (
        "I'm searching for a graph attention network that explicitly models temporal information in affordance prediction.",
        "2604.10149",
    ),  # EEG-tGAT
    (
        "Find me a reinforcement learning approach that improves image layer decomposition using VLM feedback.",
        "2605.30257",
    ),  # Stable-Layers
    (
        "I want a benchmark where digital agents need vision, search, and coding skills all at once.",
        "2604.11201",
    ),  # CocoaBench
    (
        "What's that paper about transferring useful memories between completely different coding domains?",
        "2604.14004",
    ),  # Memory Transfer Learning
    (
        "Is there a retrieval alternative to RAG where agents navigate a hierarchy instead of searching embeddings?",
        "2604.14572",
    ),  # Corpus2Skill
    (
        "Find the work showing that peer-review LLMs can outperform humans in some dimensions but still have major blind spots.",
        "2605.26730",
    ),  # PRISM
    (
        "I'm looking for a paper that unifies decision trees and diffusion models through something called Global Trajectory Score Matching. I think the title has 'Trees to Flows' in it.",
        "2605.00414",
    ),  # Trees to Flows and Back
    (
        "Find me a multi‑agent system that searches and extracts information from the whole web to produce a structured table. It uses a bi‑level architecture with an orchestrator and workers.",
        "2604.27221",
    ),  # Web2BigTable
    (
        "A method for talking head generation that uses autoregressive diffusion with separate high‑level cross‑modal reasoning and low‑level modality‑specific decoders.",
        "2604.23586",
    ),  # Talker-T2AV
    (
        "Paper about online self‑calibration for vision‑language models to reduce hallucinations. They use Monte Carlo tree search and a dual‑granularity reward mechanism.",
        "2605.00323",
    ),  # OSCAR
    (
        "Need a reinforcement learning approach where LLMs guide agents in distributed black‑box consensus optimization, with a phased cognitive scheduling strategy.",
        "2605.00691",
    ),  # LACMAS
    (
        "Something about a language‑adversarial speaker encoder for Indic cross‑script voice cloning. Uses gradient reversal to make embeddings language‑uninformative.",
        "2605.00777",
    ),  # LASE
    (
        "A structured representation for agent skills that disentangles scheduling, execution structure, and logic – called SSL. Improves skill discovery and risk assessment.",
        "2604.24026",
    ),  # SSL Representation
    (
        "Searching for a retrieval system for analog circuits that works across SPICE netlists, schematics, and descriptions. Uses a vision‑language model and a graph network.",
        "2604.23195",
    ),  # AnalogRetriever
    (
        "A reinforcement learning framework for robot policies that continues to learn during real‑world deployment by using fleet‑scale experience and human interventions. Called LWD.",
        "2605.00416",
    ),  # Learning while Deploying
    (
        "Training multilingual code reward models that can score code generation across multiple criteria and languages. They built a large preference dataset called Themis‑CodePreference.",
        "2605.00754",
    ),  # Themis
    (
        "Unified video generation framework that uses diffusion priors with stochastic condition masking and decoupled gated LoRA to handle different modalities. Name sounds like 'UniVidX'.",
        "2605.00658",
    ),  # UniVidX
    (
        "A paper about generating 3D worlds from user‑drawn segment maps – not just grid layouts. It has a detail enhancer network to add fine details while keeping global consistency.",
        "2605.00781",
    ),  # Map2World
    (
        "End‑to‑end autoregressive image generation with a 1D semantic tokenizer that jointly optimizes reconstruction and generation. Achieves FID 1.48 on ImageNet.",
        "2605.00503",
    ),  # End-to-End Autoregressive Image Generation
    (
        "Generative pre‑training for Vision Transformers that directly predicts language tokens from visual tokens using a standard language modeling objective – no contrastive loss. Called GenLIP.",
        "2605.00809",
    ),  # GenLIP
    (
        "What is that new efficient multimodal model from NVIDIA that supports audio, text, images, and video natively? It has token reduction and comes in BF16, FP8, FP4. Nemotron something?",
        "2604.24954",
    ),  # Nemotron 3 Nano Omni
    (
        "A method to make computer‑use agents faster by using a small policy by default and only calling a large model when a 'stuck monitor' or 'milestone monitor' detects risk.",
        "2604.27151",
    ),  # Step-level Optimization for Computer-use Agents
    (
        "Paper about scaling visual preference optimization. They built a huge dataset with 1M image pairs at 1024px and used a modified DPO with a polynomial term (Poly‑DPO).",
        "2604.24953",
    ),  # ViPO
    (
        "Semi‑supervised DPO that treats consistent preference pairs as clean data and conflicting ones as unlabeled, then uses pseudo‑labels. Called Semi‑DPO.",
        "2604.24952",
    ),  # Semi-DPO
    (
        "Efficient red‑teaming framework for prompt injection and knowledge corruption attacks on long‑context LLMs. Cuts runtime from one hour to under ten minutes. FlashRT.",
        "2604.28157",
    ),  # FlashRT
    (
        "I recall a paper showing that fine‑tuning foundation models for medical or legal domains unpredictably changes safety behavior – sometimes improves one metric but degrades another. 'Safety Drift'?",
        "2604.24902",
    ),  # Safety Drift After Fine-Tuning
    (
        "A dataset and method for instruction‑guided Arabic poetry generation covering both Modern Standard Arabic and dialects. They fine‑tuned LLMs and did human evaluation.",
        "2604.27766",
    ),  # Instruction-Guided Poetry Generation in Arabic
    (
        "Research about reasoning conflicts in LLMs: models prefer 'sensibility' over following explicit logical schemata. They used confidence scores to detect conflicts.",
        "2604.27251",
    ),  # Compliance versus Sensibility
    (
        "A live benchmark for workflow agents that updates over time based on real‑world demand signals. Uses execution traces and audit logs for verification. Claw‑Eval‑Live.",
        "2604.28139",
    ),  # Claw-Eval-Live
    (
        "Efficient pipeline parallelism for fine‑tuning LLMs on consumer GPUs – they treat GPUs as stateless workers and use round‑robin dispatching. Called RoundPipe.",
        "2604.27085",
    ),  # RoundPipe
    (
        "A token‑level length value model (LenVM) that predicts remaining generation length using a discounted return. Improves length control on LIFEBench and GSM8K.",
        "2604.27039",
    ),  # Length Value Model
    (
        "RLHF for image editing with a chain‑of‑thought verifier reward model. They use GRPO after training the reward model with Group Contrastive Preference Optimization.",
        "2604.27505",
    ),  # Edit-R1
    (
        "Generating humanoid robot behaviors by synthesizing third‑person videos first, then estimating motion. It's called ExoActor and generalizes without extra real‑world data.",
        "2604.27711",
    ),  # ExoActor
    (
        "A distillation method that co‑trains multiple experts in parallel – they act as mutual teachers to avoid capability loss. Works for text, image, and video reasoning.",
        "2604.27083",
    ),  # Co-Evolving Policy Distillation
    (
        "I think there's a paper about evaluating multimodal agents on interactive website generation under low‑code conditions. They use user agents with persona‑driven instruction perturbations.",
        "2604.27419",
    ),  # InteractWeb-Bench
    (
        "A new end‑to‑end motion capture method for arbitrary skeletons that avoids inverse kinematics by learning from reference pose‑rotation pairs. Reduces rotation error to ~10 degrees.",
        "2604.28130",
    ),  # MoCapAnything V2
    # =========================================================
    # NEW QUERIES — grounded in papers.md
    # =========================================================
    # --- LEVEL 1: Exact / Keyword Queries (Easy) ---
    ("SPEED-Bench speculative decoding benchmark", "2604.09557"),
    ("Introspective Diffusion Language Models ISD strided decoding", "2604.11035"),
    ("FAMA failure-aware meta-agentic framework open-source LLMs", "2604.25135"),
    ("PhyCo video diffusion physical consistency ControlNet", "2604.28169"),
    ("ArcANE character arc narrative evaluation role-playing", "2606.05553"),
    ("AdaPlanBench adaptive planning dual constraints LLM", "2606.05622"),
    ("Intern-Atlas methodological evolution graph AI literature", "2604.28158"),
    (
        "ZipSplat fewer Gaussians feed-forward scene reconstruction pose-free",
        "2606.05102",
    ),  # RE-Edit / closest; ZipSplat actual ID from file section 3291
    (
        "MedSSR medical knowledge synthesis semi-supervised reinforcement learning rare diseases",
        "2604.11547",
    ),
    ("RoundPipe pipeline parallelism consumer GPUs weight binding", "2604.27085"),
    ("CoPD Co-Evolving Policy Distillation mutual teachers", "2604.27083"),
    # --- LEVEL 2: Conversational / Problem-Solution Queries (Medium) ---
    (
        "My diffusion language model generates text much slower than autoregressive models — is there a way to close that quality gap without giving up parallel decoding?",
        "2604.11035",
    ),  # Introspective DLM
    (
        "I want to fine-tune a 70B model on eight consumer RTX 4090s without running into the weight-binding bottleneck in pipeline parallelism.",
        "2604.27085",
    ),  # RoundPipe
    (
        "How do I make my LLM agent stop catastrophically forgetting context when it operates over very long tool-use trajectories?",
        "2604.11716",
    ),  # SWE-AGILE
    (
        "I need a way to control which denoising steps in my video diffusion model handle motion versus appearance so I can compress the KV cache.",
        "2605.09681",
    ),  # Forcing-KV
    (
        "Can I train a reward model that scores code quality across Python, Java, and Go without just checking if tests pass?",
        "2605.00754",
    ),  # Themis
    (
        "My robot arm policy degrades the moment I move it to a slightly different table height. How do other people handle distribution shift after deployment?",
        "2605.00416",
    ),  # Learning While Deploying
    (
        "I'm trying to add physics consistency to my video generation model without expensive VAE decoding at every step.",
        "2603.26599",
    ),  # VGGRPO
    (
        "We have an agentic system that keeps spending thousands of dollars in a runaway retry loop. Is there a principled way to enforce token budgets at the type system level?",
        "2606.04056",  # Token Budgets paper
        # Note: ID in the markdown was found under "Token Budgets" section
    ),
    (
        "How do I translate low-resource languages that weren't in my training data without overfitting to specific seen languages?",
        "2606.06428",
    ),  # RL unseen language translation
    (
        "I want my text-to-image model to learn from human preferences but my preference dataset has a lot of label noise from conflicting annotations.",
        "2604.24952",
    ),  # Semi-DPO
    (
        "Is there a benchmark that tests whether AI agents can handle household scenarios where safety, privacy, and efficiency all pull in different directions at once?",
        "2606.03312",
    ),  # RobotValues
    (
        "I need to evaluate how well my speech model preserves retroflex sounds and vowel length in Telugu and Tamil, not just WER.",
        "2604.25476",
    ),  # PSP benchmark
    (
        "Looking for a way to build an LLM agent that gets better at data science tasks the longer it runs without manually writing more training examples.",
        "2606.03841",
    ),  # EvoDS
    (
        "My agents keep making incorrect decisions because they rely on stale memories that were invalidated by new events in the conversation.",
        "2605.06527",
    ),  # STALE
    (
        "I want to distill multiple expert models — one for math, one for code, one for visual reasoning — into a single model without losing any of their capabilities.",
        "2604.27083",
    ),  # CoPD
    (
        "How do I control the exact timing of multiple events in a video generation model so concepts don't bleed into each other?",
        "2604.10030",
    ),  # Prompt Relay
    (
        "Is there a benchmark specifically for evaluating whether LLMs can follow explicit logical schemas even when the task pattern suggests a different reasoning style?",
        "2604.27251",
    ),  # Compliance vs Sensibility
    # --- LEVEL 3: Vague / Conceptual Queries (Hard) ---
    (
        "Paper about using flow matching to train adversarially so the generator better matches the real distribution, not just MSE.",
        "2604.11521",
    ),  # Continuous Adversarial Flow Models
    (
        "Research on whether the mathematical symmetry you bake into a neural network's architecture actually helps as much as theory predicts, or if augmentation at test time closes the gap.",
        "2606.01090",
    ),  # Measuring Symmetry-Data Exchange Rate
    (
        "That paper showing LLMs discover regulatory loopholes in sandboxed social environments when trained with RL.",
        "2606.04075",
    ),  # LLMs Hack Rewards and Society
    (
        "Something about using AI to find new superconductors by screening millions of crystal structures with a mix of atomic models and language models.",
        "2604.23758",
    ),  # ElementsClaw
    (
        "I vaguely remember a paper about generating fake computers with realistic folder structures and running month-long agent simulations on them.",
        "2604.28181",
    ),  # Synthetic Computers at Scale
    (
        "How do you teach a model to think about what it doesn't know — specifically about when its own memories have gone stale.",
        "2605.06527",
    ),  # STALE
    (
        "A method for allocating inference compute across queries based on economic shadow pricing — spending less on easy queries and more on hard ones.",
        "2606.03092",
    ),  # CLEAR / Shadow Price of Reasoning
    (
        "Paper about graph attention in transformers — specifically how graph tokens behave differently from language tokens and why high-activation tokens aren't necessarily carrying graph structure.",
        "2606.03712",
    ),  # When Graph Tokens Sink
    (
        "Something about teaching robots humanoid behaviors by first generating third-person videos of the task, then estimating motion from those videos.",
        "2604.27711",
    ),  # ExoActor
    (
        "Research into whether decision trees and diffusion models are actually the same thing under some mathematical limit.",
        "2605.00414",
    ),  # Trees to Flows and Back
    (
        "A study showing that LLMs look cautious in risk tasks like the St. Petersburg paradox, but the mechanism underneath doesn't actually match how humans think about risk.",
        "2606.02993",
    ),  # Probing Outcome-Level Resemblance LLM Risk Decisions
    (
        "I want to run origami folding sequences from a text description using some kind of physics-aware planning loop.",
        "2603.29585",
    ),  # Learn2Fold
    (
        "How do you build a vision transformer pre-training that's purely generative — no contrastive loss — just predicting language tokens directly from image patches?",
        "2605.00809",
    ),  # GenLIP
    (
        "A framework for constructing agent skills that cleanly separates what triggers a skill, how it's structured, and what side effects it has.",
        "2604.24026",
    ),  # SSL Representation
    (
        "Benchmark for evaluating whether a role-playing LLM correctly evolves a character's personality across narrative arcs, not just recalls facts about them.",
        "2606.05553",
    ),  # ArcANE
    (
        "Research about how to make sense of where a chain-of-thought actually causes the model's answer versus just being decoration.",
        "2603.28590",
    ),  # MonitorBench CoT Monitorability
    # --- LEVEL 4: Highly Specific / Cross-Disciplinary (Stress Tests) ---
    (
        "An end-to-end autoregressive image model with a 1D semantic tokenizer that jointly trains the tokenizer and the generator — achieves around 1.48 FID on ImageNet 256.",
        "2605.00503",
    ),  # End-to-End Autoregressive Image Generation
    (
        "The paper that proposes treating Fréchet Distance as a differentiable training loss by decoupling the population size used for FD estimation from the mini-batch gradient computation.",
        "2604.28190",
    ),  # Representation Fréchet Loss
    (
        "A benchmark for evaluating AI agents on interactive website generation where the user instructions are deliberately ambiguous, contradictory, or redundant, simulating real non-expert users.",
        "2604.27419",
    ),  # InteractWeb-Bench
    (
        "Research showing that fine-tuning a foundation model on medical or legal data can improve safety on one dimension while silently degrading it on another — and base-model safety evaluations miss this.",
        "2604.24902",
    ),  # Safety Drift After Fine-Tuning
    (
        "I recall a paper about using gradient-reversal training to make a speaker encoder language-agnostic while remaining speaker-discriminative, tested on Indic languages.",
        "2605.00777",
    ),  # LASE
    (
        "A paper about building a citation or lineage graph across 1M AI papers to trace how methods evolve and which bottlenecks drive new innovations.",
        "2604.28158",
    ),  # Intern-Atlas
    (
        "Method for allocating capacity across specialized sub-networks in a diffusion model by partitioning the denoising timeline according to local trajectory complexity — uses something like Dirichlet energy.",
        "2606.06477",
    ),  # Complexity-Balanced Diffusion Splitting
    (
        "Semi-supervised medical image segmentation where instead of using model confidence as a quality signal, they train a separate network to predict segmentation quality from synthetic degradations.",
        "2606.01753",
    ),  # Quality-Guided SSL for Medical Image Segmentation
    (
        "A framework for running agentic systems that treats each agent as a schedulable OS process with explicit capabilities, human approval queues, and JIT tool registration.",
        "2606.03895",
    ),  # Agent libOS
    (
        "The paper that unifies text, image, video, and speech generation inside a single masked diffusion model over a shared discrete token space — no autoregressive serialization.",
        "2604.00007",
    ),  # Dynin-Omni
    (
        "I'm looking for the paper about how to merge multiple LoRA modules for different concepts without interference, using the attention weights of trigger words as a weighting signal.",
        "2606.03792",
    ),  # Training-Free Multi-Concept LoRA Composition
    (
        "Research on what properties of a cell transcriptome you can simulate using a masked discrete diffusion model — predicting gene expression changes under novel genetic perturbations.",
        "2603.25240",
    ),  # Lingshu-Cell
    (
        "Paper proposing a token-level framework where the model predicts how many tokens it still needs to generate at each step — used to improve length control without any extra annotation.",
        "2604.27039",
    ),  # Length Value Model
    (
        "A benchmark that tests code-switching ASR across unseen language pairs and finds that model merging only gives modest transfer.",
        "2606.05846",
    ),  # Towards Truly Multilingual ASR
    (
        "I think there's a paper that frames RLVR acceleration as trajectory extrapolation in the rank-1 subspace of parameter differences across LoRA training steps.",
        "2604.11446",
    ),  # NExt / Low-rank optimization trajectories
    (
        "How do you train a Vision-Language-Action model to adapt its execution pace and path in real time when the environment is moving, without any extra training?",
        "2605.11459",
    ),  # Pace-and-Path Correction for VLA
    (
        "A system that automatically edits hours of raw video footage into short rhythmic clips synchronized to music, using a multi-agent pipeline with a Playwriter and an Editor agent.",
        "2603.29664",
    ),  # CutClaw
    # --- LEVEL 5: Pure intent / topic browsing (no specific paper in mind) ---
    (
        "papers about using reinforcement learning to improve chain-of-thought reasoning in math and coding",
        "2604.09459",  # Credit Assignment survey
    ),
    (
        "methods for reducing hallucination in vision-language models",
        "2605.00323",  # OSCAR
    ),
    (
        "transformers with attention sink problems",
        "2604.10098",  # Attention Sink Survey
    ),
    (
        "equivariant neural networks for molecular or scientific data",
        "2604.09130",  # EquiformerV3 (from original set, but phrasing is new)
    ),
    (
        "speech synthesis for low-resource Indian languages",
        "2604.21481",  # Preferences of a Voice-First Nation
    ),
    (
        "federated learning with privacy guarantees on non-IID data",
        "2604.23426",  # Federated Learning with DP and Adaptive Quantization
    ),
    (
        "world models for embodied agents and 3D scene understanding",
        "2604.27578",  # World2Minecraft
    ),
    (
        "diffusion models for tabular data generation",
        "2605.00414",  # Trees to Flows and Back
    ),
    (
        "benchmark for testing AI agents on real long-horizon computer tasks",
        "2605.10912",  # WildClawBench
    ),
    (
        "how neural networks learn group structure and representations internally",
        "2606.02993",  # Neural Networks Learn Spectral Representations
    ),
    (
        "multi-agent systems for scientific discovery and autonomous research",
        "2604.23758",  # ElementsClaw
    ),
    (
        "text-to-image generation with fine-grained layout and compositional control",
        "2603.25732",  # BizGenEval
    ),
    (
        "pretraining data curation pipelines and data quality for language models",
        "2603.27164",  # daVinci-LLM
    ),
    (
        "generating 3D scenes or environments from a single image or text",
        "2603.29387",  # Extend3D
    ),
    (
        "clinical AI evaluation using standardized patient simulations",
        "2606.05112",  # MedSP1000
    ),
]
