class Program{

    public Interface IBlock{
        byte[] Data { get; }
        byte[] Hash { get; set; }
        int Nonce { get; set; }
        byte[] PrevHash { get; set; }
        DateTime TimeStamp { get; }
    }


    public class Block : IBlock
    {
        public byte[] Data { get; }
        public byte[] Hash { get; set; }
        public int Nonce { get; set; }
        public byte[] PrevHash { get; set; }
        public DateTime TimeStamp { get; }
    
        public override string ToString()
        {
            return $"{BitCoverter.ToString(Hash).Replace("-","")}:\{BitConverter.ToString(PrevHash).Replace("-","")}"\n {Nonce} {TimeStamp};
        }
    }

    public class BlockChain : IEnumerable<IBlock>
    {
        private List<IBlock> _items = new List<IBlock>();

        public BlockChain(byte[] difficulty, IBlock genesis)
        {
            Difficulty = difficulty;
            genesis.Hash = genesis.MineHas(difficulty);
            Items.add(genesis);

        }


        public void Add(IBlock item)
        {
            if(Items.LastOrDefault() != null)
            {
                item.PrevHash = Items.LastOrDefault()?.Hash;
            }
            item.Hash = item.MineHas(Difficulty);
            Items.Add(item);
        }

        public int Count => Items.Count;

        public IBlock thisp[index]{
            get => Items[index];
            set => Items[index] = value;
        }

        public List<IBlock> Items
        {
            get => _items;
            set => _items = value;
        }

        public byte[] Difficulty { get; }

        public IEnumerator<IBlock> GetEnumerator()
        {
            return Items.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return  Items.GetEnumerator();
        }
    }

    static void Main(string[] args)
    {

    }

}